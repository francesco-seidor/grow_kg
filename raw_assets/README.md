# raw_assets

Drop your source documents here, in any folder structure you like.

**Supported:** `.md` `.markdown` `.txt` `.docx` `.doc` `.rtf`

**Not supported:** PDF and PowerPoint. They are reported as unsupported rather
than silently skipped — convert them to `.docx` or `.md` to include them.

Then run `/kb-build`. Nothing in this folder is ever modified.

This README is itself skipped by the compiler (it is the only file here the
pipeline ignores by name), so you can leave it in place.
