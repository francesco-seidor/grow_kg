/* Router playground — the app behind wiki/chat.html.
 *
 * Shipped as-is: init_wiki.py copies this file to wiki/_meta/chat-app.js and
 * chat.html loads it with a script tag. It never fetches — the whole corpus
 * arrives as window.__KB_CHAT__ from _meta/chat-data.js, loaded the same way,
 * because fetch() of a sibling file is blocked on file:// and a script tag is
 * not. So the page still works from a double-click, with no server.
 *
 * The one idea worth keeping in mind while reading: the model returns SCORES,
 * and this file decides what passes. Floors and keep-counts are applied here,
 * never by the model, which is what makes them movable without re-prompting.
 */
(function () {
  "use strict";

  // No payload is not a failure — it is the state of a wiki nobody has compiled
  // yet. The viewer ships before its data does, so leave the boot banner up and
  // say what to run.
  var PAYLOAD = window.__KB_CHAT__;
  if (!PAYLOAD || typeof PAYLOAD !== "object" || !PAYLOAD.nodes) {
    console.warn("no window.__KB_CHAT__ — _meta/chat-data.js is missing or failed to load");
    return;
  }
  var SDK = window.AnthropicSDK || null;
  var NS = "kbchat:" + (PAYLOAD.content_hash || "nohash");

  // ------------------------------------------------------------------
  // model capabilities — the only place a model fact lives
  // ------------------------------------------------------------------
  var EFFORTS = ["low", "medium", "high", "xhigh", "max"];
  var MODELS = [
    { id: "claude-opus-5",    label: "Opus 5",    efforts: EFFORTS, thinking: "adaptive",
      cacheMin: 512,  priceIn: 5,  priceOut: 25 },
    { id: "claude-opus-4-8",  label: "Opus 4.8",  efforts: EFFORTS, thinking: "adaptive",
      cacheMin: 1024, priceIn: 5,  priceOut: 25 },
    { id: "claude-sonnet-5",  label: "Sonnet 5",  efforts: EFFORTS, thinking: "adaptive",
      cacheMin: 1024, priceIn: 2,  priceOut: 10 },
    { id: "claude-haiku-4-5", label: "Haiku 4.5", efforts: [],      thinking: "budget",
      cacheMin: 4096, priceIn: 1,  priceOut: 5 },
    { id: "claude-fable-5-1", label: "Fable 5.1", efforts: EFFORTS, thinking: "always",
      cacheMin: 512,  priceIn: 10, priceOut: 50 }
  ];

  function capability(id) {
    for (var i = 0; i < MODELS.length; i++) if (MODELS[i].id === id) return MODELS[i];
    return null;
  }

  // ------------------------------------------------------------------
  // default prompts
  // ------------------------------------------------------------------
  var PROMPTS = {
    layer1:
      "You are layer 1 of a two-layer retrieval router over a compiled knowledge base.\n" +
      "You are given every category in the base, each with a one-sentence description of " +
      "the questions it answers.\n\n" +
      "Score EVERY category listed, including the obviously irrelevant ones. Use the full " +
      "range:\n" +
      "  0.9-1.0  the description directly covers what was asked\n" +
      "  0.6-0.8  plausibly covers it; the answer is likely in here\n" +
      "  0.3-0.5  same broad area, but probably not where the answer lives\n" +
      "  0.0-0.2  only topically adjacent, or unrelated\n\n" +
      "Judge by the description, not by the category name. Also return one short sentence " +
      "of what you understood the question to be asking.",
    layer2:
      "You are layer 2 of a two-layer retrieval router over a compiled knowledge base.\n" +
      "You are given candidate notes, each with a one-sentence description of the questions " +
      "it answers.\n\n" +
      "Score EVERY note listed. Use the full range:\n" +
      "  0.9-1.0  this note's description directly answers the question\n" +
      "  0.6-0.8  this note probably contains the answer\n" +
      "  0.3-0.5  related, but would not answer it on its own\n" +
      "  0.0-0.2  wrong note\n\n" +
      "A note answers a question when its description says so; do not guess at content the " +
      "description does not claim. Also return one short sentence of what you understood " +
      "the question to be asking.",
    answer:
      "You answer questions from a compiled knowledge base. You are given the full text of " +
      "the notes the router selected.\n\n" +
      "Rules:\n" +
      "- Answer ONLY from the notes provided. You have no other source. Do not fill gaps " +
      "from general knowledge.\n" +
      "- Never state a number, date, threshold, entitlement or version that is not written " +
      "in the notes.\n" +
      "- Cite the note path(s) you answered from, e.g. `01-leave-and-absence/parental-leave.md`.\n" +
      "- If a note carries a Conflict callout covering what was asked, present BOTH versions " +
      "as unresolved and say a human decision is needed. Never pick one.\n" +
      "- If a note you relied on is marked content_confidence: low, say so.\n" +
      "- If the notes do not answer the question, say plainly that the knowledge base does " +
      "not cover it, and name the closest notes. Do not pad."
  };

  // ------------------------------------------------------------------
  // settings
  // ------------------------------------------------------------------
  function baseStage(model, effort, thinking, maxTokens) {
    return { model: model, effort: effort, thinking: thinking,
             thinking_budget: 2048, max_tokens: maxTokens };
  }

  function defaultPreset() {
    var d = PAYLOAD.defaults || {};
    return {
      label: "Default — two-layer, Opus 5",
      mode: "two_layer",
      layer1: merge(baseStage("claude-opus-5", "low", false, 4000),
                    { keep: d.layer1_keep || 3, floor: 0.25 }),
      layer2: merge(baseStage("claude-opus-5", "low", false, 4000),
                    { keep: d.layer2_keep || 5, floor: 0.45 }),
      answer: baseStage("claude-opus-5", "high", true, 8000),
      fallback: "refuse",
      escalate_model: "claude-opus-5",
      cache: "auto",
      include_deprecated: false,
      flat_max_input_tokens: 60000,
      bm25: { k1: 1.5, b: 0.75 },
      prompts: { layer1: PROMPTS.layer1, layer2: PROMPTS.layer2, answer: PROMPTS.answer }
    };
  }

  function seedPresets() {
    var base = defaultPreset();
    var cheap = clone(base);
    cheap.label = "Cheap router — Haiku L1, Sonnet L2, Opus answer";
    // No effort on Haiku — it takes budget_tokens, and an effort field would 400.
    cheap.layer1.model = "claude-haiku-4-5"; cheap.layer1.effort = null;
    cheap.layer2.model = "claude-sonnet-5"; cheap.layer2.effort = "low";
    var flat = clone(base); flat.label = "Flat one-shot"; flat.mode = "flat";
    var bm = clone(base); bm.label = "BM25 baseline"; bm.mode = "bm25";
    bm.layer1.floor = 0.35; bm.layer2.floor = 0.35;
    var ro = clone(base); ro.label = "Retrieve only — no synthesis";
    ro.answer.model = "none";
    return { version: 1, active: "default",
             presets: { "default": base, "cheap-router": cheap, "flat-oneshot": flat,
                        "bm25-baseline": bm, "retrieve-only": ro } };
  }

  function clone(v) { return JSON.parse(JSON.stringify(v)); }
  function merge(a, b) { for (var k in b) if (b.hasOwnProperty(k)) a[k] = b[k]; return a; }

  var storeWarned = false;
  var memStore = {};
  function lsGet(key) {
    try { var v = window.localStorage.getItem(key); return v; }
    catch (e) { noteStoreFailure(); return memStore[key] === undefined ? null : memStore[key]; }
  }
  function lsSet(key, value) {
    try { window.localStorage.setItem(key, value); }
    catch (e) { noteStoreFailure(); memStore[key] = value; }
  }
  function lsDel(key) {
    try { window.localStorage.removeItem(key); } catch (e) { delete memStore[key]; }
  }
  function noteStoreFailure() {
    if (storeWarned) return;
    storeWarned = true;
    banner("This browser is not letting the page save settings (common on file:// in " +
           "Safari). Settings will work for this session only — use Export settings to " +
           "keep them, or serve the folder with <code>python3 -m http.server</code>.");
  }

  var CLAMPS = {
    keep: [1, 20], floor: [0, 1], max_tokens: [256, 64000],
    thinking_budget: [1024, 32000], flat_max_input_tokens: [1000, 400000],
    k1: [0, 3], b: [0, 1]
  };

  function clampNum(value, range, fallback) {
    var n = typeof value === "number" ? value : parseFloat(value);
    if (isNaN(n)) return fallback;
    return Math.min(range[1], Math.max(range[0], n));
  }

  /* Coerce a preset into something the API will actually accept. Runs on load
   * and on save, so a hand-edited or stale preset degrades instead of 400ing. */
  function sanitizePreset(p, notes) {
    var d = defaultPreset();
    p = p && typeof p === "object" ? p : {};
    var out = clone(d);
    out.label = typeof p.label === "string" ? p.label : d.label;
    out.mode = ["two_layer", "flat", "bm25"].indexOf(p.mode) >= 0 ? p.mode : d.mode;
    out.fallback = ["refuse", "answer_anyway", "widen", "escalate", "bm25_rescue"]
      .indexOf(p.fallback) >= 0 ? p.fallback : d.fallback;
    out.cache = ["auto", "on", "off"].indexOf(p.cache) >= 0 ? p.cache : d.cache;
    out.include_deprecated = !!p.include_deprecated;
    out.flat_max_input_tokens = clampNum(p.flat_max_input_tokens,
      CLAMPS.flat_max_input_tokens, d.flat_max_input_tokens);
    out.bm25 = { k1: clampNum((p.bm25 || {}).k1, CLAMPS.k1, d.bm25.k1),
                 b: clampNum((p.bm25 || {}).b, CLAMPS.b, d.bm25.b) };
    out.escalate_model = capability(p.escalate_model) ? p.escalate_model : d.escalate_model;

    ["layer1", "layer2", "answer"].forEach(function (name) {
      var src = p[name] || {};
      var dst = out[name];
      var allowNone = name === "answer";
      var cap = capability(src.model);
      if (src.model === "none" && allowNone) {
        dst.model = "none";
      } else if (!cap) {
        if (src.model) notes.push(name + ": unknown model “" + src.model +
                                  "” → " + dst.model);
      } else {
        dst.model = src.model;
      }
      cap = capability(dst.model);
      dst.max_tokens = clampNum(src.max_tokens, CLAMPS.max_tokens, dst.max_tokens);
      dst.thinking = !!src.thinking;
      dst.thinking_budget = clampNum(src.thinking_budget, CLAMPS.thinking_budget,
                                     dst.thinking_budget);
      if (cap) {
        if (src.effort && cap.efforts.length === 0) {
          notes.push(name + ": " + cap.label + " takes no effort setting → dropped");
          dst.effort = null;
        } else if (cap.efforts.length === 0) {
          dst.effort = null;
        } else if (src.effort && cap.efforts.indexOf(src.effort) < 0) {
          notes.push(name + ": effort “" + src.effort + "” not valid for " +
                     cap.label + " → " + dst.effort);
        } else if (src.effort) {
          dst.effort = src.effort;
        }
        if (dst.thinking && cap.thinking === "always") {
          notes.push(name + ": " + cap.label + " always thinks; the toggle does nothing");
        }
      }
      if (name !== "answer") {
        dst.keep = Math.round(clampNum(src.keep, CLAMPS.keep, dst.keep));
        dst.floor = clampNum(src.floor, CLAMPS.floor, dst.floor);
      }
    });

    var pr = p.prompts || {};
    out.prompts = {
      layer1: typeof pr.layer1 === "string" && pr.layer1.trim() ? pr.layer1 : PROMPTS.layer1,
      layer2: typeof pr.layer2 === "string" && pr.layer2.trim() ? pr.layer2 : PROMPTS.layer2,
      answer: typeof pr.answer === "string" && pr.answer.trim() ? pr.answer : PROMPTS.answer
    };
    return out;
  }

  function loadSettings() {
    var raw = lsGet(NS + ":settings");
    var doc = null;
    if (raw) { try { doc = JSON.parse(raw); } catch (e) { doc = null; } }
    if (!doc || doc.version !== 1 || !doc.presets) {
      if (raw) banner("Stored settings were unreadable — starting from the defaults.");
      // Sanitize the seeds too: the shipped presets must be held to the same
      // capability rules as anything a user or an import produces.
      doc = seedPresets();
    }
    var notes = [];
    var out = { version: 1, active: doc.active, presets: {} };
    Object.keys(doc.presets).forEach(function (k) {
      out.presets[k] = sanitizePreset(doc.presets[k], notes);
    });
    if (!out.presets["default"]) out.presets["default"] = defaultPreset();
    if (!out.presets[out.active]) out.active = "default";
    if (notes.length) banner("Adjusted stored settings: " + notes.join("; "));
    return out;
  }

  function saveSettings() {
    lsSet(NS + ":settings", JSON.stringify(SETTINGS));
  }

  /* Identity fingerprint for a preset, so a run log entry says which settings
   * produced it. Not a security hash — crypto.subtle is async and unavailable
   * in some file:// contexts, so this is a plain synchronous FNV-1a. */
  function fingerprint(obj) {
    var s = JSON.stringify(obj, Object.keys(obj).sort());
    function fnv(seed) {
      var h = seed >>> 0;
      for (var i = 0; i < s.length; i++) {
        h ^= s.charCodeAt(i);
        h = (h + (h << 1) + (h << 4) + (h << 7) + (h << 8) + (h << 24)) >>> 0;
      }
      return ("00000000" + h.toString(16)).slice(-8);
    }
    return (fnv(0x811c9dc5) + fnv(0x01000193)).slice(0, 12);
  }

  var SETTINGS = loadSettings();
  function active() { return SETTINGS.presets[SETTINGS.active]; }

  // ------------------------------------------------------------------
  // corpus
  // ------------------------------------------------------------------
  var NODES_BY_ID = {};
  PAYLOAD.nodes.forEach(function (n) { NODES_BY_ID[n.id] = n; });

  function corpusNodes(includeDeprecated) {
    return PAYLOAD.nodes.filter(function (n) {
      return includeDeprecated || n.status !== "deprecated";
    });
  }

  function nodesInClusters(slugs, includeDeprecated) {
    var want = {};
    slugs.forEach(function (s) { want[s] = true; });
    return corpusNodes(includeDeprecated).filter(function (n) { return want[n.cluster]; });
  }

  // ------------------------------------------------------------------
  // candidate blocks — deterministic bytes for a given corpus
  // ------------------------------------------------------------------
  function kwPart(list) {
    return list && list.length ? " | keywords: " + list.join(", ") : "";
  }

  function clusterBlock() {
    return PAYLOAD.categories.slice().sort(function (a, b) {
      return a.slug < b.slug ? -1 : 1;
    }).map(function (c) {
      return c.slug + " | " + c.title + " — " + c.description + kwPart(c.keywords);
    }).join("\n");
  }

  function nodeBlock(nodes) {
    return nodes.slice().sort(function (a, b) { return a.id < b.id ? -1 : 1; })
      .map(function (n) {
        return n.id + " | " + n.title + " — " + n.description +
               kwPart((n.keywords || []).concat(n.aliases || []));
      }).join("\n");
  }

  function answerContext(nodes) {
    return nodes.map(function (n) {
      return "=== " + n.path + " ===\n" +
             "title: " + n.title + "\n" +
             "cluster: " + n.cluster + "\n" +
             "status: " + n.status + "\n" +
             "content_confidence: " + n.content_confidence + "\n" +
             "updated: " + (n.updated || "unknown") + "\n" +
             "sources: " + ((n.sources || []).join("; ") || "none listed") + "\n\n" +
             n.body;
    }).join("\n\n");
  }

  // ------------------------------------------------------------------
  // schema + ranking
  // ------------------------------------------------------------------
  /* The enum is the point: pinning `key` to the real identifier set makes a
   * hallucinated route structurally impossible. Numeric and array constraints
   * (minimum/maximum/minItems) are rejected by structured outputs, so `score`
   * is bounded by the prompt and then clamped in rank(). */
  function scoreSchema(keys) {
    return {
      type: "object",
      additionalProperties: false,
      required: ["interpretation", "candidates"],
      properties: {
        interpretation: { type: "string" },
        candidates: {
          type: "array",
          items: {
            type: "object",
            additionalProperties: false,
            required: ["key", "score", "reason"],
            properties: {
              key: { type: "string", enum: keys },
              score: { type: "number" },
              reason: { type: "string" }
            }
          }
        }
      }
    };
  }

  /* clamp -> dedupe -> sort -> truncate to keep -> apply floor.
   * The floor last, so a below-floor item can never occupy one of the slots. */
  function rank(items, validIds, keep, floor, relative) {
    var seen = {};
    (items || []).forEach(function (it) {
      var id = it && it.key;
      if (!id || !validIds[id]) return;
      var s = parseFloat(it.score);
      if (isNaN(s)) s = 0;
      s = Math.min(1, Math.max(0, s));
      if (!seen[id] || s > seen[id].score) {
        seen[id] = { id: id, score: s, reason: String(it.reason || "") };
      }
    });
    var ordered = Object.keys(seen).map(function (k) { return seen[k]; })
      .sort(function (a, b) { return b.score - a.score; });
    var cut = (relative && ordered.length) ? floor * ordered[0].score : floor;
    var head = ordered.slice(0, keep);
    // `score > 0` matters for the relative cut: when nothing matched, every
    // score is 0 and the cut is 0, so `>=` alone would keep the entire corpus.
    var passes = function (d) { return d.score >= cut && (!relative || d.score > 0); };
    var kept = head.filter(passes);
    var dropped = head.filter(function (d) { return !passes(d); })
      .map(function (d) { return merge(clone(d), { why: "below_floor" }); })
      .concat(ordered.slice(keep).map(function (d) {
        return merge(clone(d), { why: "beyond_keep" });
      }));
    return { kept: kept, dropped: dropped, cut: cut, ordered: ordered };
  }

  // ------------------------------------------------------------------
  // BM25
  // ------------------------------------------------------------------
  var STOP = ("a an and are as at be by can do does for from get got has have how i in is it " +
    "its me my of on or our so than that the their them then there these this to was we what " +
    "when where which who why will with you your").split(" ").reduce(function (m, w) {
      m[w] = true; return m;
    }, {});

  function fold(t) {
    var pairs = [["ies", "y"], ["es", ""], ["s", ""]];
    for (var i = 0; i < pairs.length; i++) {
      var suf = pairs[i][0], repl = pairs[i][1];
      if (t.length > suf.length && t.slice(-suf.length) === suf &&
          t.length - suf.length + repl.length >= 3) {
        return t.slice(0, t.length - suf.length) + repl;
      }
    }
    return t;
  }

  function tokenize(text) {
    var norm = String(text || "").normalize("NFKD").replace(/[̀-ͯ]/g, "")
      .toLowerCase();
    var raw = norm.match(/[a-z0-9]+/g) || [];
    var out = [];
    for (var i = 0; i < raw.length; i++) {
      var t = raw[i];
      if (t.length < 2 || STOP[t]) continue;
      out.push(fold(t));
    }
    return out;
  }

  var bm25Cache = {};
  function bm25Index(docs, cacheKey) {
    if (bm25Cache[cacheKey]) return bm25Cache[cacheKey];
    var df = {}, total = 0;
    var entries = docs.map(function (d) {
      var toks = tokenize(d.text);
      var tf = {};
      toks.forEach(function (t) { tf[t] = (tf[t] || 0) + 1; });
      Object.keys(tf).forEach(function (t) { df[t] = (df[t] || 0) + 1; });
      total += toks.length;
      return { id: d.id, tf: tf, len: toks.length };
    });
    var idx = { entries: entries, df: df, n: entries.length,
                avgdl: entries.length ? total / entries.length : 0 };
    bm25Cache[cacheKey] = idx;
    return idx;
  }

  function bm25Score(idx, query, k1, b) {
    var qt = tokenize(query);
    var uniq = {};
    qt.forEach(function (t) { uniq[t] = true; });
    var terms = Object.keys(uniq);
    return idx.entries.map(function (e) {
      var total = 0, ev = [];
      terms.forEach(function (t) {
        var f = e.tf[t] || 0;
        if (!f) return;
        var nq = idx.df[t] || 0;
        var idf = Math.log(1 + (idx.n - nq + 0.5) / (nq + 0.5));
        var denom = f + k1 * (1 - b + b * (idx.avgdl ? e.len / idx.avgdl : 1));
        var contrib = idf * (f * (k1 + 1)) / denom;
        total += contrib;
        ev.push({ term: t, idf: round(idf, 3), tf: f, contrib: round(contrib, 3) });
      });
      ev.sort(function (x, y) { return y.contrib - x.contrib; });
      return { key: e.id, raw: round(total, 4), evidence: ev.slice(0, 5) };
    }).sort(function (a, b2) { return b2.raw - a.raw; });
  }

  function round(n, places) {
    var f = Math.pow(10, places);
    return Math.round(n * f) / f;
  }

  // ------------------------------------------------------------------
  // API
  // ------------------------------------------------------------------
  var apiKey = null;
  var client = null;

  function setKey(key, remember) {
    apiKey = key && key.trim() ? key.trim() : null;
    client = null;
    if (remember && apiKey) lsSet(NS + ":key", apiKey);
    if (!remember) lsDel(NS + ":key");
    renderKeyState();
  }

  function getClient() {
    if (!SDK) throw new Error("The Anthropic SDK did not load — this page cannot call the API.");
    if (!apiKey) throw new Error("No API key set. Paste one in the admin panel.");
    if (!client) client = new SDK.Anthropic({ apiKey: apiKey, dangerouslyAllowBrowser: true });
    return client;
  }

  function redact(text) {
    return String(text == null ? "" : text)
      .replace(/sk-ant-[A-Za-z0-9_\-]{8,}/g, "sk-ant-***");
  }

  /* Single choke point for every request. Illegal parameter combinations are
   * impossible by construction: an effort the table does not list is dropped,
   * thinking is shaped by the model family, and temperature has no code path
   * at all (it is removed API-wide on current models). */
  function buildRequest(stage, parts) {
    var cap = capability(stage.model);
    if (!cap) throw new Error("Unknown model: " + stage.model);
    var req = {
      model: stage.model,
      max_tokens: stage.max_tokens,
      system: parts.system,
      messages: parts.messages
    };
    if (cap.thinking === "adaptive" && stage.thinking) {
      req.thinking = { type: "adaptive" };
    } else if (cap.thinking === "budget" && stage.thinking) {
      var budget = Math.max(1024, stage.thinking_budget || 1024);
      req.thinking = { type: "enabled", budget_tokens: budget };
      req.max_tokens = Math.max(req.max_tokens, budget + 2048);
    }
    // cap.thinking === "always" (Fable): send nothing; any explicit value 400s.
    var oc = {};
    if (cap.efforts.length && stage.effort && cap.efforts.indexOf(stage.effort) >= 0) {
      oc.effort = stage.effort;
    }
    if (parts.schema) oc.format = { type: "json_schema", schema: parts.schema };
    if (Object.keys(oc).length) req.output_config = oc;
    return req;
  }

  function estTokens(text) { return Math.ceil(String(text || "").length / 4); }

  var tokenCache = {};
  function countTokens(model, system, messages) {
    var key = model + "|" + fingerprint({ s: system, m: messages });
    if (tokenCache[key] !== undefined) return Promise.resolve(tokenCache[key]);
    return getClient().messages.countTokens({ model: model, system: system, messages: messages })
      .then(function (r) { tokenCache[key] = r.input_tokens; return r.input_tokens; })
      .catch(function () {
        var fallback = estTokens(JSON.stringify(system) + JSON.stringify(messages));
        tokenCache[key] = fallback;
        return fallback;
      });
  }

  /* Static instructions first, the volatile candidate list second with the
   * breakpoint on it, the question last in messages. `auto` only attaches the
   * breakpoint when the block clears this model's minimum — below it, caching
   * silently never fires, which is why the trace reports cache tokens. */
  function systemBlocks(stage, instructions, block, cacheMode) {
    var cap = capability(stage.model);
    var blocks = [{ type: "text", text: instructions }];
    var b = { type: "text", text: block };
    var want = cacheMode === "on" ||
      (cacheMode === "auto" && cap && estTokens(block) >= cap.cacheMin);
    if (want) b.cache_control = { type: "ephemeral" };
    blocks.push(b);
    return blocks;
  }

  function classifyError(err) {
    var out = { kind: "unknown", status: null, message: redact(err && err.message),
                retryable: false, hint: "" };
    if (!SDK) return out;
    if (err instanceof SDK.AuthenticationError) {
      out.kind = "auth"; out.status = 401;
      out.hint = "The API key was rejected. Check it, or paste a different one.";
    } else if (err instanceof SDK.PermissionDeniedError) {
      out.kind = "permission"; out.status = 403;
      out.hint = "This key lacks permission for that request.";
    } else if (err instanceof SDK.NotFoundError) {
      out.kind = "not_found"; out.status = 404;
      out.hint = "That model is probably not available to your organisation.";
    } else if (err instanceof SDK.BadRequestError) {
      out.kind = "bad_request"; out.status = 400;
      out.hint = "Usually an illegal parameter for this model — the message above " +
                 "names it. Check effort and thinking for this stage.";
    } else if (err instanceof SDK.RateLimitError) {
      out.kind = "rate_limit"; out.status = 429; out.retryable = true;
      var ra = err.headers && (err.headers.get ? err.headers.get("retry-after")
                                               : err.headers["retry-after"]);
      out.hint = ra ? "Rate limited — retry after " + ra + "s." : "Rate limited.";
    } else if (err instanceof SDK.APIConnectionTimeoutError) {
      out.kind = "timeout"; out.retryable = true;
      out.hint = "The request timed out. Lower effort or max tokens.";
    } else if (err instanceof SDK.APIConnectionError) {
      out.kind = "connection"; out.retryable = true;
      out.hint = "Could not reach the API. Check the network.";
    } else if (err instanceof SDK.APIError) {
      out.kind = "api"; out.status = err.status || null;
      out.retryable = !!(err.status && err.status >= 500);
    }
    return out;
  }

  function usageOf(msg) {
    var u = (msg && msg.usage) || {};
    return {
      input_tokens: u.input_tokens || 0,
      output_tokens: u.output_tokens || 0,
      cache_read_input_tokens: u.cache_read_input_tokens || 0,
      cache_creation_input_tokens: u.cache_creation_input_tokens || 0
    };
  }

  function costOf(model, usage) {
    var cap = capability(model);
    if (!cap) return 0;
    var inTok = usage.input_tokens + usage.cache_creation_input_tokens * 1.25 +
                usage.cache_read_input_tokens * 0.1;
    return (inTok * cap.priceIn + usage.output_tokens * cap.priceOut) / 1e6;
  }

  function firstText(msg) {
    var blocks = (msg && msg.content) || [];
    for (var i = 0; i < blocks.length; i++) {
      if (blocks[i].type === "text") return blocks[i].text;
    }
    return "";
  }

  // ------------------------------------------------------------------
  // scoring stage
  // ------------------------------------------------------------------
  function scoreStage(opts) {
    var stage = opts.stage;
    var system = systemBlocks(stage, opts.instructions, opts.block, opts.cache);
    var messages = [{ role: "user", content: opts.question }];
    var req = buildRequest(stage, { system: system, messages: messages,
                                    schema: scoreSchema(opts.keys) });
    var started = Date.now();
    return getClient().messages.create(req).then(function (msg) {
      var parsed = { interpretation: "", candidates: [] };
      try { parsed = JSON.parse(firstText(msg)) || parsed; } catch (e) { /* keep empty */ }
      var usage = usageOf(msg);
      return {
        ms: Date.now() - started,
        model: stage.model,
        effort: (req.output_config || {}).effort || null,
        thinking: !!req.thinking,
        cached_breakpoint: system.length > 1 && !!system[1].cache_control,
        interpretation: String(parsed.interpretation || ""),
        candidates: parsed.candidates || [],
        usage: usage,
        cost_usd: costOf(stage.model, usage),
        context_system: system.map(function (b) { return b.text; }).join("\n\n"),
        context_user: opts.question
      };
    });
  }

  // ------------------------------------------------------------------
  // diagnosis
  // ------------------------------------------------------------------
  function diagnose(t) {
    var l1 = t.layer1, l2 = t.layer2;
    function tight(ordered) {
      return ordered && ordered.length >= 2 &&
             Math.abs(ordered[0].score - ordered[1].score) <= 0.05;
    }
    if (t.mode === "bm25" && t.bm25) {
      return { code: "no_keyword_match",
               text: "No word in the question appears in any note's title, description, " +
                     "keywords or aliases. Either the base does not cover this, or the " +
                     "vocabulary the notes use differs from the question's — try the " +
                     "two-layer router, which matches on meaning rather than words." };
    }
    if (l1 && tight(l1.ordered)) {
      return { code: "overlapping_descriptions",
               text: "Layer 1 is coin-flipping between “" + label(l1.ordered[0].id) +
                     "” and “" + label(l1.ordered[1].id) + "” (" +
                     l1.ordered[0].score.toFixed(2) + " vs " +
                     l1.ordered[1].score.toFixed(2) + "). Fix the taxonomy boundary, " +
                     "not the wording." };
    }
    if (l2 && tight(l2.ordered)) {
      return { code: "overlapping_nodes",
               text: "Two notes split the signal (" + l2.ordered[0].id + " vs " +
                     l2.ordered[1].id + "). Merge them, or sharpen the boundary between " +
                     "their descriptions." };
    }
    if (l1 && l1.kept && l1.kept.length && l2) {
      return { code: "missing_content",
               text: "The right category exists but nothing in it answers this. Best note " +
                     "scored " + (l2.ordered[0] ? l2.ordered[0].score.toFixed(2) : "0.00") +
                     ". This is a content gap, not a description problem." };
    }
    return { code: "missing_cluster_or_weak_descriptions",
             text: "No category cleared the layer-1 floor. Either the base has no category " +
                   "for this, or the category descriptions do not say that they cover it." };
  }

  function label(slug) {
    for (var i = 0; i < PAYLOAD.categories.length; i++) {
      if (PAYLOAD.categories[i].slug === slug) return PAYLOAD.categories[i].title;
    }
    return slug;
  }

  // ------------------------------------------------------------------
  // orchestration
  // ------------------------------------------------------------------
  function retrieve(question, cfg, trace) {
    if (cfg.mode === "bm25") return retrieveBm25(question, cfg, trace);
    if (cfg.mode === "flat") return retrieveFlat(question, cfg, trace);
    return retrieveTwoLayer(question, cfg, trace);
  }

  function retrieveBm25(question, cfg, trace) {
    var nodes = corpusNodes(cfg.include_deprecated);
    var idx = bm25Index(nodes.map(function (n) {
      return { id: n.id, text: n.embedding_text };
    }), "nodes|" + cfg.include_deprecated);
    var scored = bm25Score(idx, question, cfg.bm25.k1, cfg.bm25.b);
    var top = scored.length ? scored[0].raw : 0;
    var evidence = {};
    // Normalise against the top hit so the floor means the same thing as
    // elsewhere in the UI: BM25 scores are unbounded and corpus-dependent.
    var items = scored.map(function (s) {
      evidence[s.key] = s.evidence;
      return { key: s.key, score: top > 0 ? s.raw / top : 0,
               reason: s.evidence.length
                 ? "matched " + s.evidence.map(function (e) { return e.term; }).join(", ")
                 : "no query term matched" };
    });
    var valid = {};
    nodes.forEach(function (n) { valid[n.id] = true; });
    var r = rank(items, valid, cfg.layer2.keep, cfg.layer2.floor, true);
    r.kept.forEach(function (k) { k.evidence = evidence[k.id]; });
    r.dropped.forEach(function (k) { k.evidence = evidence[k.id]; });
    var note = "Relative floor: kept when score ≥ " + cfg.layer2.floor +
      " × top score. Top raw BM25 score was " + round(top, 3) + ".";
    note += top > 0
      // Worth saying plainly: normalising against the top hit means the winner
      // always scores 1.0, so raising this floor prunes runners-up and never
      // the winner. Only a zero-match query refuses here.
      ? " A relative floor never rejects the top hit — it only prunes runners-up."
      : " No query term matched anything in the base, so nothing was kept.";
    trace.stages.push({
      stage: "bm25", model: "(none — keyword scoring)", ms: 0,
      floor: cfg.layer2.floor, floor_kind: "relative", cut: r.cut,
      usage: usageOf(null), cost_usd: 0, candidates: nodes.length,
      picks: r.kept, dropped: r.dropped.slice(0, 8), note: note
    });
    trace.bm25 = r;
    return Promise.resolve({ nodes: r.kept.map(function (k) { return NODES_BY_ID[k.id]; }),
                             deciding: r, layerName: "bm25" });
  }

  function retrieveFlat(question, cfg, trace) {
    var nodes = corpusNodes(cfg.include_deprecated);
    var block = nodeBlock(nodes);
    var keys = nodes.map(function (n) { return n.id; });
    var budget = cfg.flat_max_input_tokens;
    var system = systemBlocks(cfg.layer2, cfg.prompts.layer2, block, cfg.cache);
    var messages = [{ role: "user", content: question }];

    if (keys.length > 2000) {
      return Promise.reject(guardError(
        "Flat mode would send " + keys.length + " candidate ids in one schema, which is " +
        "past what is workable. Switch to the two-layer router or BM25."));
    }
    return countTokens(cfg.layer2.model, system, messages).then(function (est) {
      if (est > budget) {
        return Promise.reject(guardError(
          "Flat mode needs about " + est.toLocaleString() + " input tokens for " +
          nodes.length + " notes, over the " + budget.toLocaleString() + " budget. " +
          "Raise the flat budget, switch to the two-layer router, or use BM25."));
      }
      if (est > budget * 0.5) {
        trace.notices.push({ level: "warning", text:
          "Flat mode is using about " + est.toLocaleString() + " input tokens (" +
          Math.round(100 * est / budget) + "% of budget) on every question." });
      }
      var valid = {};
      keys.forEach(function (k) { valid[k] = true; });
      return scoreStage({ stage: cfg.layer2, instructions: cfg.prompts.layer2,
                          block: block, keys: keys, question: question, cache: cfg.cache })
        .then(function (res) {
          var r = rank(res.candidates, valid, cfg.layer2.keep, cfg.layer2.floor, false);
          pushScoreStage(trace, "flat", res, r, cfg.layer2.floor, keys.length);
          trace.layer2 = r;
          return { nodes: r.kept.map(function (k) { return NODES_BY_ID[k.id]; }),
                   deciding: r, layerName: "flat" };
        });
    });
  }

  function guardError(text) {
    var e = new Error(text);
    e.kbGuard = true;
    return e;
  }

  function pushScoreStage(trace, name, res, r, floor, candidates) {
    trace.stages.push({
      stage: name, model: res.model, effort: res.effort, thinking: res.thinking,
      ms: res.ms, candidates: candidates, interpretation: res.interpretation,
      floor: floor, floor_kind: "absolute", cut: r.cut,
      usage: res.usage, cost_usd: res.cost_usd,
      cached_breakpoint: res.cached_breakpoint,
      picks: r.kept, dropped: r.dropped.slice(0, 8),
      context_system: res.context_system, context_user: res.context_user
    });
  }

  function retrieveTwoLayer(question, cfg, trace) {
    var cats = PAYLOAD.categories;
    var slugs = cats.map(function (c) { return c.slug; });
    var validCats = {};
    slugs.forEach(function (s) { validCats[s] = true; });

    return scoreStage({ stage: cfg.layer1, instructions: cfg.prompts.layer1,
                        block: clusterBlock(), keys: slugs, question: question,
                        cache: cfg.cache })
      .then(function (res1) {
        var r1 = rank(res1.candidates, validCats, cfg.layer1.keep, cfg.layer1.floor, false);
        pushScoreStage(trace, "layer1", res1, r1, cfg.layer1.floor, slugs.length);
        trace.layer1 = r1;

        if (!r1.kept.length) {
          return { nodes: [], deciding: r1, layerName: "layer1" };
        }
        return layer2Pass(question, cfg, trace, r1, cfg.layer2, "layer2");
      });
  }

  /* One layer-2 call over the UNION of the kept clusters' nodes. Separate calls
   * per cluster would produce scores from different contexts, and merging those
   * by score is meaningless. */
  function layer2Pass(question, cfg, trace, r1, stage, name) {
    var nodes = nodesInClusters(r1.kept.map(function (k) { return k.id; }),
                                cfg.include_deprecated);
    if (!nodes.length) {
      var empty = { kept: [], dropped: [], cut: stage.floor, ordered: [] };
      trace.notices.push({ level: "warning", text:
        "The kept categories contain no eligible notes" +
        (cfg.include_deprecated ? "." : " (deprecated notes are excluded).") });
      trace.layer2 = empty;
      return { nodes: [], deciding: empty, layerName: name };
    }
    var valid = {};
    nodes.forEach(function (n) { valid[n.id] = true; });
    return scoreStage({ stage: stage, instructions: cfg.prompts.layer2,
                        block: nodeBlock(nodes), keys: nodes.map(function (n) { return n.id; }),
                        question: question, cache: cfg.cache })
      .then(function (res2) {
        var r2 = rank(res2.candidates, valid, stage.keep, stage.floor, false);
        pushScoreStage(trace, name, res2, r2, stage.floor, nodes.length);
        trace.layer2 = r2;
        return { nodes: r2.kept.map(function (k) { return NODES_BY_ID[k.id]; }),
                 deciding: r2, layerName: name };
      });
  }

  // ------------------------------------------------------------------
  // fallbacks
  // ------------------------------------------------------------------
  function applyFallback(question, cfg, trace, result) {
    if (result.nodes.length) return Promise.resolve(result);
    var mode = cfg.fallback;

    if (mode === "answer_anyway") {
      var head = (result.deciding.ordered || []).slice(0, cfg.layer2.keep);
      var nodes = head.map(function (d) { return NODES_BY_ID[d.id]; })
        .filter(function (n) { return !!n; });
      if (nodes.length) {
        trace.forced = true;
        trace.notices.push({ level: "warning", text:
          "Nothing cleared the floor. Answering anyway from the top " + nodes.length +
          " note(s) — treat this answer as low confidence." });
        return Promise.resolve({ nodes: nodes, deciding: result.deciding,
                                 layerName: result.layerName });
      }
    }

    if (mode === "widen" && trace.layer1 && trace.layer1.kept.length &&
        cfg.mode === "two_layer") {
      var wider = clone(cfg.layer2);
      wider.keep = Math.min(CLAMPS.keep[1], cfg.layer2.keep * 2);
      wider.floor = cfg.layer2.floor * 0.5;
      trace.notices.push({ level: "warning", text:
        "Nothing cleared " + cfg.layer2.floor.toFixed(2) + " — retrying layer 2 at keep " +
        wider.keep + ", floor " + wider.floor.toFixed(2) + "." });
      return layer2Pass(question, cfg, trace, trace.layer1, wider, "layer2.retry");
    }

    if (mode === "escalate") {
      var esc = clone(result.layerName === "layer1" ? cfg.layer1 : cfg.layer2);
      esc.model = cfg.escalate_model;
      esc.effort = capability(esc.model) && capability(esc.model).efforts.length
        ? "high" : null;
      trace.notices.push({ level: "warning", text:
        "Nothing cleared the floor — re-running " + result.layerName + " on " +
        (capability(esc.model) || {}).label + " at high effort to tell a weak router " +
        "apart from missing content." });
      if (result.layerName === "layer1") {
        var slugs = PAYLOAD.categories.map(function (c) { return c.slug; });
        var validCats = {};
        slugs.forEach(function (s) { validCats[s] = true; });
        return scoreStage({ stage: esc, instructions: cfg.prompts.layer1,
                            block: clusterBlock(), keys: slugs, question: question,
                            cache: cfg.cache })
          .then(function (res) {
            var r = rank(res.candidates, validCats, esc.keep, esc.floor, false);
            pushScoreStage(trace, "layer1.escalated", res, r, esc.floor, slugs.length);
            trace.layer1 = r;
            if (!r.kept.length) return { nodes: [], deciding: r, layerName: "layer1" };
            return layer2Pass(question, cfg, trace, r, cfg.layer2, "layer2");
          });
      }
      return layer2Pass(question, cfg, trace, trace.layer1 ||
        { kept: PAYLOAD.categories.map(function (c) { return { id: c.slug }; }) },
        esc, "layer2.escalated");
    }

    if (mode === "bm25_rescue" && cfg.mode !== "bm25") {
      trace.notices.push({ level: "warning", text:
        "Nothing cleared the floor — falling back to BM25 over the whole base." });
      return retrieveBm25(question, cfg, trace).then(function (r) {
        trace.rescued = true;
        return r;
      });
    }

    return Promise.resolve(result);
  }

  // ------------------------------------------------------------------
  // answering
  // ------------------------------------------------------------------
  function refusalText(cfg, trace, result) {
    var d = diagnose(trace);
    trace.diagnosis = d;
    var near = (result.deciding.ordered || []).slice(0, 3);
    var lines = ["The knowledge base does not cover this."];
    if (near.length) {
      lines.push("");
      lines.push("Closest notes considered:");
      near.forEach(function (n) {
        var node = NODES_BY_ID[n.id];
        lines.push("  • " + (node ? node.path : n.id) + "  (" + n.score.toFixed(2) +
                   ")  " + n.reason);
      });
    }
    lines.push("");
    lines.push("Diagnosis — " + d.code + ": " + d.text);
    return lines.join("\n");
  }

  function answer(question, cfg, trace, result, onDelta) {
    if (!result.nodes.length) {
      trace.refused = true;
      return Promise.resolve({ text: refusalText(cfg, trace, result), streamed: false });
    }
    if (cfg.answer.model === "none") {
      trace.retrieve_only = true;
      var lines = ["Retrieve-only mode — no synthesis call was made.", "", "Routed to:"];
      result.nodes.forEach(function (n) {
        lines.push("  • " + n.path + "  — " + n.description);
      });
      return Promise.resolve({ text: lines.join("\n"), streamed: false });
    }

    var ctx = answerContext(result.nodes);
    var instructions = cfg.prompts.answer + (trace.forced
      ? "\n\nThe router was NOT confident these notes answer the question. Say so before " +
        "answering, and do not overstate what the notes support."
      : "");
    var system = systemBlocks(cfg.answer, instructions, ctx, cfg.cache);
    var messages = [{ role: "user", content: question }];
    var req = buildRequest(cfg.answer, { system: system, messages: messages });
    var started = Date.now();

    trace.context = {
      nodes: result.nodes.map(function (n) {
        return { path: n.path, title: n.title, cluster: n.cluster, status: n.status,
                 content_confidence: n.content_confidence, chars: n.body.length,
                 has_conflict: n.has_conflict, updated: n.updated };
      }),
      chars: ctx.length,
      tokens_est: estTokens(ctx),
      system: system.map(function (b) { return b.text; }).join("\n\n"),
      user: question
    };

    var stream = getClient().messages.stream(req);
    var acc = "";
    stream.on("text", function (t) { acc += t; onDelta(acc); });
    return stream.finalMessage().then(function (msg) {
      var usage = usageOf(msg);
      trace.stages.push({
        stage: "answer", model: cfg.answer.model,
        effort: (req.output_config || {}).effort || null, thinking: !!req.thinking,
        ms: Date.now() - started, usage: usage, cost_usd: costOf(cfg.answer.model, usage),
        cached_breakpoint: system.length > 1 && !!system[1].cache_control,
        stop_reason: msg.stop_reason,
        context_system: trace.context.system, context_user: question
      });
      if (msg.stop_reason === "refusal") {
        trace.notices.push({ level: "warning", text:
          "The model declined to answer (stop_reason: refusal)." });
      }
      return { text: acc || firstText(msg), streamed: true };
    });
  }

  // ------------------------------------------------------------------
  // run
  // ------------------------------------------------------------------
  var running = false;

  function ask(question) {
    if (running) return;
    var cfg = clone(active());
    var digest = fingerprint(cfg);
    var trace = { stages: [], notices: [], started: Date.now(),
                  mode: cfg.mode, preset: SETTINGS.active, settings_digest: digest };

    running = true;
    setBusy(true);
    addMessage("user", question);
    var view = addMessage("assistant", "");
    var bubble = view.bubble;
    bubble.textContent = "…";

    retrieve(question, cfg, trace)
      .then(function (result) { return applyFallback(question, cfg, trace, result); })
      .then(function (result) {
        return answer(question, cfg, trace, result, function (partial) {
          bubble.textContent = partial;
          scrollThread();
        });
      })
      .then(function (out) {
        bubble.textContent = out.text;
        finish(trace, view, true);
      })
      .catch(function (err) {
        if (err && err.kbGuard) {
          bubble.textContent = err.message;
          trace.guard = err.message;
        } else {
          var info = classifyError(err);
          bubble.textContent = "That run failed. See the trace below.";
          trace.error = info;
          if (!SDK) trace.error.hint = "The SDK did not load into this page.";
        }
        finish(trace, view, false);
      });
  }

  function finish(trace, view, ok) {
    trace.ms = Date.now() - trace.started;
    trace.ok = ok;
    view.trace.appendChild(renderTrace(trace));
    logRun(trace);
    running = false;
    setBusy(false);
    scrollThread();
  }

  function logRun(trace) {
    var entry = {
      ts: new Date().toISOString(), ok: trace.ok, ms: trace.ms, mode: trace.mode,
      preset: trace.preset, settings_digest: trace.settings_digest,
      refused: !!trace.refused, forced: !!trace.forced, rescued: !!trace.rescued,
      diagnosis: trace.diagnosis ? trace.diagnosis.code : null,
      route: (trace.context ? trace.context.nodes.map(function (n) { return n.path; }) : []),
      totals: totalsOf(trace),
      error: trace.error ? { kind: trace.error.kind, status: trace.error.status } : null
    };
    var raw = lsGet(NS + ":runs");
    var list = [];
    if (raw) { try { list = JSON.parse(raw) || []; } catch (e) { list = []; } }
    list.push(entry);
    if (list.length > 300) list = list.slice(-300);
    lsSet(NS + ":runs", JSON.stringify(list));
  }

  function totalsOf(trace) {
    var t = { input_tokens: 0, output_tokens: 0, cache_read_input_tokens: 0,
              cache_creation_input_tokens: 0, cost_usd: 0 };
    trace.stages.forEach(function (s) {
      t.input_tokens += s.usage.input_tokens;
      t.output_tokens += s.usage.output_tokens;
      t.cache_read_input_tokens += s.usage.cache_read_input_tokens;
      t.cache_creation_input_tokens += s.usage.cache_creation_input_tokens;
      t.cost_usd += s.cost_usd || 0;
    });
    t.cost_usd = round(t.cost_usd, 5);
    return t;
  }

  // ------------------------------------------------------------------
  // rendering
  // ------------------------------------------------------------------
  var thread = document.getElementById("thread");

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined && text !== null) e.textContent = text;
    return e;
  }

  function addMessage(who, text) {
    var wrap = el("div", "msg " + who);
    wrap.appendChild(el("div", "who", who === "user" ? "you" : "knowledge base"));
    var bubble = el("div", "bubble", text);
    wrap.appendChild(bubble);
    var traceHost = el("div");
    wrap.appendChild(traceHost);
    thread.appendChild(wrap);
    scrollThread();
    return { bubble: bubble, trace: traceHost };
  }

  function scrollThread() { thread.scrollTop = thread.scrollHeight; }

  function chip(text, cls) { return el("span", "chip" + (cls ? " " + cls : ""), text); }

  function renderTrace(trace) {
    var box = el("div", "trace");
    var ribbon = el("div", "ribbon");

    ribbon.appendChild(chip(trace.mode.replace("_", "-"), trace.ok ? "" : "bad"));
    trace.stages.forEach(function (s) {
      var bits = s.stage + " " + s.ms + "ms";
      if (s.usage.input_tokens || s.usage.output_tokens) {
        bits += " · " + s.usage.input_tokens + "→" + s.usage.output_tokens;
      }
      ribbon.appendChild(chip(bits));
      if (s.usage.cache_read_input_tokens) {
        ribbon.appendChild(chip("cache ✓ " + s.usage.cache_read_input_tokens, "cache"));
      } else if (s.cached_breakpoint) {
        ribbon.appendChild(chip("cache write " + s.usage.cache_creation_input_tokens, "cache"));
      }
    });
    var totals = totalsOf(trace);
    if (totals.cost_usd) ribbon.appendChild(chip("$" + totals.cost_usd.toFixed(5), "ok"));
    if (trace.refused) ribbon.appendChild(chip("refused", "warn"));
    if (trace.forced) ribbon.appendChild(chip("forced", "warn"));
    if (trace.rescued) ribbon.appendChild(chip("bm25 rescue", "warn"));
    if (trace.retrieve_only) ribbon.appendChild(chip("retrieve-only", "warn"));
    ribbon.appendChild(chip(trace.preset + " · " + trace.settings_digest));
    box.appendChild(ribbon);

    if (trace.error) {
      var card = el("div", "errcard");
      card.appendChild(el("b", null, (trace.error.kind || "error") +
        (trace.error.status ? " (" + trace.error.status + ")" : "")));
      card.appendChild(el("div", null, trace.error.message || ""));
      if (trace.error.hint) card.appendChild(el("div", "small", trace.error.hint));
      box.appendChild(card);
    }
    if (trace.guard) {
      var g = el("div", "notice");
      g.appendChild(el("b", null, "guard"));
      g.appendChild(el("div", null, trace.guard));
      box.appendChild(g);
    }
    trace.notices.forEach(function (n) {
      box.appendChild(el("div", "notice", n.text));
    });

    trace.stages.forEach(function (s) { box.appendChild(renderStage(s)); });

    if (trace.context) {
      var d = el("details");
      d.appendChild(el("summary", null, "context handed to the answer model · " +
        trace.context.nodes.length + " note(s), ~" + trace.context.tokens_est + " tokens"));
      var body = el("div", "body");
      trace.context.nodes.forEach(function (n) {
        var line = el("div", "small");
        line.textContent = n.path + "  · " + n.chars + " chars" +
          (n.content_confidence === "low" ? "  · content_confidence: low" : "") +
          (n.has_conflict ? "  · has an open conflict" : "") +
          (n.status === "deprecated" ? "  · deprecated" : "");
        body.appendChild(line);
      });
      var pre = el("div", "ctx", trace.context.system + "\n\n--- user ---\n" +
                   trace.context.user);
      body.appendChild(pre);
      var row = el("div", "btnrow");
      var copy = el("button", null, "Copy exact context");
      copy.onclick = function () {
        copyText(trace.context.system + "\n\n--- user ---\n" + trace.context.user, copy);
      };
      row.appendChild(copy);
      body.appendChild(row);
      d.appendChild(body);
      box.appendChild(d);
    }
    return box;
  }

  function renderStage(s) {
    var d = el("details");
    var head = s.stage + " · " + s.model +
      (s.effort ? " · effort " + s.effort : "") +
      (s.candidates ? " · " + s.candidates + " candidates" : "") +
      (s.cut !== undefined ? " · cut " + Number(s.cut).toFixed(2) : "");
    d.appendChild(el("summary", null, head));
    var body = el("div", "body");

    if (s.interpretation) {
      body.appendChild(el("p", "small", "read as: “" + s.interpretation + "”"));
    }
    if (s.note) body.appendChild(el("p", "small", s.note));

    if (s.picks) {
      var table = el("table", "cands");
      var thead = el("thead");
      var hr = el("tr");
      ["", "score", "id", "why"].forEach(function (h) {
        hr.appendChild(el("th", null, h));
      });
      thead.appendChild(hr);
      table.appendChild(thead);
      var tb = el("tbody");
      s.picks.forEach(function (p) { tb.appendChild(candRow(p, true)); });
      (s.dropped || []).forEach(function (p) { tb.appendChild(candRow(p, false)); });
      table.appendChild(tb);
      body.appendChild(table);
    }

    if (s.context_system) {
      var cd = el("details");
      cd.appendChild(el("summary", null, "exact prompt for this stage"));
      var cb = el("div", "body");
      cb.appendChild(el("div", "ctx", s.context_system + "\n\n--- user ---\n" +
                        s.context_user));
      var row = el("div", "btnrow");
      var copy = el("button", null, "Copy");
      copy.onclick = function () {
        copyText(s.context_system + "\n\n--- user ---\n" + s.context_user, copy);
      };
      row.appendChild(copy);
      cb.appendChild(row);
      cd.appendChild(cb);
      body.appendChild(cd);
    }
    d.appendChild(body);
    return d;
  }

  function candRow(p, kept) {
    var tr = el("tr", kept ? "" : "cut");
    tr.appendChild(el("td", null, kept ? "✓" : "✕"));
    tr.appendChild(el("td", "score", p.score.toFixed(2)));
    var node = NODES_BY_ID[p.id];
    tr.appendChild(el("td", null, node ? node.path : p.id));
    var why = p.reason || "";
    if (!kept && p.why) why = "[" + p.why.replace("_", " ") + "] " + why;
    if (p.evidence && p.evidence.length) {
      why += "  · " + p.evidence.map(function (e) {
        return e.term + "(" + e.contrib + ")";
      }).join(" ");
    }
    if (node && node.content_confidence === "low") why += "  · content_confidence: low";
    tr.appendChild(el("td", null, why));
    return tr;
  }

  function copyText(text, btn) {
    var done = function () {
      var old = btn.textContent;
      btn.textContent = "Copied";
      setTimeout(function () { btn.textContent = old; }, 1200);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { showModal("Copy", text); });
    } else {
      showModal("Copy", text);
    }
  }

  // ------------------------------------------------------------------
  // admin panel
  // ------------------------------------------------------------------
  function $(id) { return document.getElementById(id); }

  function banner(html, bad) {
    var b = el("div", "banner" + (bad ? " bad" : ""));
    b.innerHTML = html;
    $("banners").appendChild(b);
  }

  var STAGE_META = [
    { key: "layer1", title: "Layer 1 router (clusters)" },
    { key: "layer2", title: "Layer 2 router (notes)" },
    { key: "answer", title: "Answer synthesiser" }
  ];

  function modelOptions(select, allowNone) {
    select.innerHTML = "";
    if (allowNone) {
      var none = el("option", null, "None — retrieve only");
      none.value = "none";
      select.appendChild(none);
    }
    MODELS.forEach(function (m) {
      var o = el("option", null, m.label);
      o.value = m.id;
      select.appendChild(o);
    });
  }

  function buildStages() {
    var host = $("stages");
    host.innerHTML = "";
    STAGE_META.forEach(function (meta) {
      var wrap = el("div", "stage");
      wrap.appendChild(el("h3", null, meta.title));

      var rowM = el("div", "row");
      rowM.appendChild(el("label", null, "Model"));
      var sel = el("select");
      sel.id = meta.key + "-model";
      modelOptions(sel, meta.key === "answer");
      rowM.appendChild(sel);
      wrap.appendChild(rowM);

      var rowE = el("div", "row");
      rowE.id = meta.key + "-effort-row";
      rowE.appendChild(el("label", null, "Effort"));
      var eff = el("select");
      eff.id = meta.key + "-effort";
      EFFORTS.forEach(function (v) {
        var o = el("option", null, v); o.value = v; eff.appendChild(o);
      });
      rowE.appendChild(eff);
      wrap.appendChild(rowE);

      var rowT = el("div", "row");
      rowT.id = meta.key + "-thinking-row";
      rowT.appendChild(el("label", null, "Extended thinking"));
      var th = el("input");
      th.type = "checkbox";
      th.id = meta.key + "-thinking";
      rowT.appendChild(th);
      wrap.appendChild(rowT);

      var rowB = el("div", "row");
      rowB.id = meta.key + "-budget-row";
      rowB.appendChild(el("label", null, "Thinking budget"));
      var bud = el("input");
      bud.type = "number"; bud.min = "1024"; bud.step = "512";
      bud.id = meta.key + "-budget";
      rowB.appendChild(bud);
      wrap.appendChild(rowB);

      var rowMt = el("div", "row");
      rowMt.appendChild(el("label", null, "Max tokens"));
      var mt = el("input");
      mt.type = "number"; mt.min = "256"; mt.step = "256";
      mt.id = meta.key + "-maxtokens";
      rowMt.appendChild(mt);
      wrap.appendChild(rowMt);

      host.appendChild(wrap);

      // The thinking toggle changes which controls are legal, so it re-renders.
      sel.onchange = th.onchange = function () { readForm(); renderForm(); };
      [eff, bud, mt].forEach(function (c) { c.onchange = readForm; });
    });

    var host2 = $("prompts");
    host2.innerHTML = "";
    STAGE_META.forEach(function (meta) {
      var wrap = el("div", "stage");
      wrap.appendChild(el("h3", null, meta.title));
      var ta = el("textarea", "prompt");
      ta.id = meta.key + "-prompt";
      ta.onchange = readForm;
      wrap.appendChild(ta);
      var row = el("div", "btnrow");
      var reset = el("button", null, "Reset to default");
      reset.onclick = function () {
        active().prompts[meta.key] = PROMPTS[meta.key];
        saveSettings();
        renderForm();
      };
      row.appendChild(reset);
      wrap.appendChild(row);
      host2.appendChild(wrap);
    });

    modelOptions($("escalate-model"), false);
  }

  function renderPresetSelect() {
    var sel = $("preset-select");
    sel.innerHTML = "";
    Object.keys(SETTINGS.presets).forEach(function (k) {
      var o = el("option", null, SETTINGS.presets[k].label + "  (" + k + ")");
      o.value = k;
      sel.appendChild(o);
    });
    sel.value = SETTINGS.active;
  }

  function renderForm() {
    var c = active();
    $("mode").value = c.mode;
    $("l1-keep").value = c.layer1.keep;
    $("l1-floor").value = c.layer1.floor;
    $("l2-keep").value = c.layer2.keep;
    $("l2-floor").value = c.layer2.floor;
    $("fallback").value = c.fallback;
    $("escalate-model").value = c.escalate_model;
    $("include-deprecated").checked = !!c.include_deprecated;
    $("cache").value = c.cache;
    $("flat-budget").value = c.flat_max_input_tokens;
    $("bm25-k1").value = c.bm25.k1;
    $("bm25-b").value = c.bm25.b;

    // BM25 floors are relative to the top hit; absolute floors are meaningless
    // against unbounded, corpus-dependent scores.
    var rel = c.mode === "bm25";
    $("l1-floor-label").textContent = rel ? "Layer 1 — floor (unused in BM25)"
                                          : "Layer 1 — floor";
    $("l2-floor-label").textContent = rel ? "Floor (× top score)" : "Layer 2 — floor";

    STAGE_META.forEach(function (meta) {
      var s = c[meta.key];
      $(meta.key + "-model").value = s.model;
      var cap = capability(s.model);
      var effRow = $(meta.key + "-effort-row");
      var thRow = $(meta.key + "-thinking-row");
      var budRow = $(meta.key + "-budget-row");
      if (!cap) {
        effRow.hidden = thRow.hidden = budRow.hidden = true;
      } else {
        effRow.hidden = cap.efforts.length === 0;
        if (!effRow.hidden) $(meta.key + "-effort").value = s.effort || "high";
        thRow.hidden = cap.thinking === "always";
        $(meta.key + "-thinking").checked = !!s.thinking;
        budRow.hidden = !(cap.thinking === "budget" && s.thinking);
        $(meta.key + "-budget").value = s.thinking_budget;
      }
      $(meta.key + "-maxtokens").value = s.max_tokens;
      $(meta.key + "-prompt").value = c.prompts[meta.key];
    });

    $("preset-digest").textContent = "fingerprint " + fingerprint(c);
    renderKeyState();
  }

  function readForm() {
    var c = active();
    c.mode = $("mode").value;
    c.layer1.keep = parseInt($("l1-keep").value, 10);
    c.layer1.floor = parseFloat($("l1-floor").value);
    c.layer2.keep = parseInt($("l2-keep").value, 10);
    c.layer2.floor = parseFloat($("l2-floor").value);
    c.fallback = $("fallback").value;
    c.escalate_model = $("escalate-model").value;
    c.include_deprecated = $("include-deprecated").checked;
    c.cache = $("cache").value;
    c.flat_max_input_tokens = parseInt($("flat-budget").value, 10);
    c.bm25.k1 = parseFloat($("bm25-k1").value);
    c.bm25.b = parseFloat($("bm25-b").value);

    STAGE_META.forEach(function (meta) {
      var s = c[meta.key];
      s.model = $(meta.key + "-model").value;
      var cap = capability(s.model);
      s.effort = cap && cap.efforts.length ? $(meta.key + "-effort").value : null;
      s.thinking = $(meta.key + "-thinking").checked;
      s.thinking_budget = parseInt($(meta.key + "-budget").value, 10) || 2048;
      s.max_tokens = parseInt($(meta.key + "-maxtokens").value, 10);
      c.prompts[meta.key] = $(meta.key + "-prompt").value;
    });

    var notes = [];
    SETTINGS.presets[SETTINGS.active] = sanitizePreset(c, notes);
    saveSettings();
    $("preset-digest").textContent = "fingerprint " +
      fingerprint(SETTINGS.presets[SETTINGS.active]);
    if (notes.length) banner("Adjusted: " + notes.join("; "));
  }

  function renderKeyState() {
    var s = $("key-state");
    if (!SDK) {
      s.textContent = "The SDK did not load — the page cannot call the API.";
      return;
    }
    if (!apiKey) {
      s.textContent = "No key set. BM25 mode and the retrieve-only preset work without one.";
      return;
    }
    s.textContent = "Key set (…" + apiKey.slice(-4) + "). Kept in memory" +
      ($("key-remember").checked ? " and in this browser." : " for this session only.");
  }

  function showModal(title, text) {
    $("modal-title").textContent = title;
    $("modal-text").value = text;
    $("modal").showModal();
  }

  function exportForKbAsk() {
    var c = active();
    var lines = [
      "<!-- router settings, tuned in wiki/chat.html -->",
      "",
      "Route with these parameters:",
      "",
      "- mode: " + c.mode,
      "- layer 1: keep at most " + c.layer1.keep + " categor" +
        (c.layer1.keep === 1 ? "y" : "ies") + " scoring ≥ " + c.layer1.floor,
      "- layer 2: keep at most " + c.layer2.keep + " note(s) scoring ≥ " + c.layer2.floor +
        ", scored in ONE pass over the union of the kept categories' notes",
      "- below the floor: " + c.fallback,
      "- deprecated notes: " + (c.include_deprecated ? "included" : "excluded"),
      "",
      "Score every candidate 0.0-1.0 and apply the floors yourself after scoring;",
      "do not let the scoring step decide what passes.",
      "",
      "## Layer 1 prompt", "", c.prompts.layer1, "",
      "## Layer 2 prompt", "", c.prompts.layer2, "",
      "## Answer prompt", "", c.prompts.answer, ""
    ];
    showModal("Paste into .claude/commands/kb-ask.md", lines.join("\n"));
  }

  function download(name, text, type) {
    var blob = new Blob([text], { type: type || "application/json" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url; a.download = name;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  }

  // ------------------------------------------------------------------
  // wiring
  // ------------------------------------------------------------------
  function setBusy(busy) {
    $("send").disabled = busy;
    $("send").textContent = busy ? "Thinking…" : "Ask";
  }

  function init() {
    var boot = document.getElementById("boot");
    if (boot) boot.hidden = true;
    document.getElementById("app").hidden = false;
    if (PAYLOAD.title) {
      document.title = PAYLOAD.title;
      $("chat-title").textContent = PAYLOAD.title;
    }

    var t = PAYLOAD.totals;
    $("head-meta").textContent = t.nodes + " notes · " + t.clusters + " categories" +
      (t.deprecated_nodes ? " · " + t.deprecated_nodes + " deprecated" : "") +
      (PAYLOAD.content_hash ? " · " + PAYLOAD.content_hash : "");
    $("vault-stats").textContent = PAYLOAD.vault + " · compiled " +
      PAYLOAD.generated + " · " + t.nodes + " notes, " + t.clusters +
      " categories, " + t.conflicts + " open conflict(s)";
    $("composer-hint").textContent =
      "Answers come only from this vault. Enter sends; Shift+Enter adds a line.";

    if (!t.nodes) {
      banner("This vault has no notes. Compile one with <code>/kb-build</code>, then " +
             "regenerate this page.", true);
    }
    if (t.missing_bodies) {
      banner(t.missing_bodies + " note(s) had no body on disk and cannot be answered from.",
             true);
    }
    if (!SDK) {
      banner("The Anthropic SDK did not load, so only BM25 mode and the retrieve-only " +
             "preset will work. Rebuild this page with a vendored SDK.", true);
    }

    buildStages();
    renderPresetSelect();
    renderForm();

    var saved = lsGet(NS + ":key");
    if (saved) {
      apiKey = saved;
      $("api-key").value = saved;
      $("key-remember").checked = true;
      renderKeyState();
    }

    $("api-key").onchange = function () {
      setKey($("api-key").value, $("key-remember").checked);
    };
    $("key-remember").onchange = function () {
      setKey($("api-key").value, $("key-remember").checked);
    };

    ["mode", "l1-keep", "l1-floor", "l2-keep", "l2-floor", "fallback", "escalate-model",
     "include-deprecated", "cache", "flat-budget", "bm25-k1", "bm25-b"].forEach(function (id) {
      $(id).onchange = function () { readForm(); renderForm(); };
    });

    $("preset-select").onchange = function () {
      SETTINGS.active = $("preset-select").value;
      saveSettings();
      renderForm();
    };
    $("preset-save").onclick = function () { readForm(); banner("Preset saved."); };
    $("preset-dup").onclick = function () {
      var name = window.prompt("Name for the new preset (short, no spaces):", "");
      if (!name) return;
      var key = name.trim().toLowerCase().replace(/[^a-z0-9-]+/g, "-");
      if (!key) return;
      var copy = clone(active());
      copy.label = name.trim();
      SETTINGS.presets[key] = copy;
      SETTINGS.active = key;
      saveSettings();
      renderPresetSelect();
      renderForm();
    };
    $("preset-del").onclick = function () {
      if (SETTINGS.active === "default") {
        banner("The default preset cannot be deleted.", true);
        return;
      }
      delete SETTINGS.presets[SETTINGS.active];
      SETTINGS.active = "default";
      saveSettings();
      renderPresetSelect();
      renderForm();
    };
    $("preset-reset").onclick = function () {
      SETTINGS.presets[SETTINGS.active] = SETTINGS.active === "default"
        ? defaultPreset() : clone(seedPresets().presets[SETTINGS.active] || defaultPreset());
      saveSettings();
      renderForm();
      banner("Preset reverted to its shipped values.");
    };

    $("export-kbask").onclick = exportForKbAsk;
    $("export-settings").onclick = function () {
      // Deliberately no key: presets are meant to be shared and diffed.
      download("kbchat-settings.json", JSON.stringify(SETTINGS, null, 2));
    };
    $("import-settings").onclick = function () {
      var input = document.createElement("input");
      input.type = "file";
      input.accept = "application/json,.json";
      input.onchange = function () {
        var f = input.files && input.files[0];
        if (!f) return;
        var r = new FileReader();
        r.onload = function () {
          try {
            var doc = JSON.parse(String(r.result));
            var notes = [];
            var out = { version: 1, active: doc.active || "default", presets: {} };
            Object.keys(doc.presets || {}).forEach(function (k) {
              out.presets[k] = sanitizePreset(doc.presets[k], notes);
            });
            if (!Object.keys(out.presets).length) throw new Error("no presets in that file");
            if (!out.presets[out.active]) out.active = Object.keys(out.presets)[0];
            SETTINGS = out;
            saveSettings();
            renderPresetSelect();
            renderForm();
            banner("Imported " + Object.keys(out.presets).length + " preset(s)." +
                   (notes.length ? " Adjusted: " + notes.join("; ") : ""));
          } catch (e) {
            banner("That file could not be imported: " + redact(e.message), true);
          }
        };
        r.readAsText(f);
      };
      input.click();
    };
    $("download-runs").onclick = function () {
      var raw = lsGet(NS + ":runs");
      var list = [];
      if (raw) { try { list = JSON.parse(raw) || []; } catch (e) { list = []; } }
      if (!list.length) { banner("No runs logged yet."); return; }
      download("kbchat-runs.jsonl", list.map(function (r) {
        return JSON.stringify(r);
      }).join("\n") + "\n", "application/x-ndjson");
    };

    $("modal-ok").onclick = function () { $("modal").close(); };
    $("modal-copy").onclick = function () {
      $("modal-text").select();
      copyText($("modal-text").value, $("modal-copy"));
    };

    var q = $("q");
    q.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter" && !ev.shiftKey) {
        ev.preventDefault();
        $("ask-form").requestSubmit ? $("ask-form").requestSubmit()
                                    : $("ask-form").dispatchEvent(new Event("submit"));
      }
    });
    $("ask-form").addEventListener("submit", function (ev) {
      ev.preventDefault();
      var text = q.value.trim();
      if (!text || running) return;
      q.value = "";
      ask(text);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
