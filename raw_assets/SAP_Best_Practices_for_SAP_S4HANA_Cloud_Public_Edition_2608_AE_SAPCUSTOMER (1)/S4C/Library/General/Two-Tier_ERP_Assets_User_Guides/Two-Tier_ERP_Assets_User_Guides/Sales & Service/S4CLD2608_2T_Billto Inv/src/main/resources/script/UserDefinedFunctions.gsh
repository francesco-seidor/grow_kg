import com.sap.gateway.ip.core.customdev.util.Message;
import java.util.*;
import com.sap.it.api.mapping.*;
import com.sap.it.api.mapping.MappingContext;


//This method splits a string based on character length, expects two input parameters: Source field which needs to be split(textLines) 
//and number of characters after which it has to be split(chunkSize)

public void splitText(String[] textLines, int[] chunkSize, Output output){

	for(String textLine: textLines){
       
        int arraySize = (int) Math.ceil(textLine.length() / chunkSize[0]);
 
    	String[] returnArray = new String[arraySize];
 
    	int index = 0;
    	for(int i = 0; i < textLine.length(); i = i+chunkSize[0])
    	{
        	if(textLine.length() - i < chunkSize[0])
        	{
            returnArray[index++] = textLine.substring(i);
        	} 
        	else
        	{
            returnArray[index++] = textLine.substring(i, i+chunkSize[0]);
        	}
    	}


        for(String value: returnArray)
        {
        	output.addValue(value);
        }        
	} 
}

//This method checks if a value exists in an array, expects two input parameters: Source field (inputValues) 
//and value which needs to be checked in array(checkString)

public void existsInArray(String[] inputValues, String[] checkString, Output output){
	for(int i=0;i<inputValues.length;i++){
		if(inputValues[i].equals(checkString[0]))
		{
		output.addValue(true);
		break;
	}       
} 
output.addValue(false);
}

//This method checks if a value exists in an array and if true, returns a corresponding value of any arbitrary element of the array:
//expects three input parameters: Search element of the array(inputValues), the value which needs to be checked in array(checkString)
//and the element from which the output value should be retrieved(outputValue)

public void getArrayValue(String[] inputValues, String[] checkString, String[] outputValue, Output output){
	for(int i=0;i<inputValues.length;i++){
		if(inputValues[i].equals(checkString[0])){
		output.addValue(outputValue[i]);
		return;
		}
	}
}

//This method checks whether a string contains a character pattern, expects two input parameters: string (textLine) 
//and character pattern(checkPattern) which needs to be checked in string. Returns true or false

public void stringContains(String[] textLine, String[] checkPattern, Output output){

 for(int i=0;i<textLine.length;i++){  
	if(textLine[i].contains(checkPattern[0])){
		output.addValue(true);
		} else {       
		output.addValue(false);
		}
	}
}

//This method checks whether RELOBJ_TYPE CUAN_INTER exists, if true returns the RELOBJ_OBJKEY, else blank 

public void checkRelObjType(String[] relobj_type, String[] relobj_objkey, Output output){
	for(int i=0;i<relobj_type.length;i++){
		if(relobj_type[i].equals("CUAN_INTER")){
		output.addValue(relobj_objkey[i]);
		return;
		}
	}
		output.addValue(" ");
}

//This method returns value of a property, expects one input prop_name i.e. name of the property to be retrieved
def String get_property(String prop_name,MappingContext context) {

    def prop = context.getProperty(prop_name);

    return prop;

}

//This method returns value of a header, expects one input header_name i.e. name of the header to be retrieved
def String get_header(String header_name,MappingContext context) {

    def header = context.getHeader(header_name);

    return header;

}

def String generateUUID(String input) {

    String uuid = UUID.randomUUID().toString().replaceAll("-","").toUpperCase();

    return uuid;

}

def String getOffset(String input, int offset) {
    if(input.equals(""))
    return input;
    else
    def string_offset = input.substring(offset,input.length);
    return string_offset;

}

//Method for OneOrder ContactID
public void checkPartnerNo(String[] main_partner, String[] partner_pft, String[] partner_no, Output output){
	for(int i=0;i<main_partner.length;i++){
		if(main_partner[i].equals("X") & partner_pft[i].equals("0007")){
		output.addValue(partner_no[i]);
		return;
		}
	}
	for(int i=0;i<main_partner.length;i++){
		if(main_partner[i].equals("X") & partner_pft[i].equals("0006")){
		output.addValue(partner_no[i]);
		return;
		}
	}
	for(int i=0;i<main_partner.length;i++){
		if((main_partner[i].equals("X")) & (!partner_pft[i].equals("0005")) & (!partner_pft[i].equals("0008"))){
		output.addValue(partner_no[i]);
		return;
		} 
	}
	output.addValue("");
}
