import re

dict_decrypt={
                "48":"1",
                "4B":"2",
                "4A":"3",
                "4D":"4",
                "4C":"5",
                "4F":"6",
                "4E":"7",
                "41":"8",
                "40":"9",
                "49":"0",
                "38":"A",
                "3B":"B",
                "3A":"C",
                "3D":"D",
                "3C":"E",
                "3F":"F",
                "3E":"G",
                "31":"H",
                "30":"I",
                "33":"J",
                "32":"K",
                "35":"L",
                "34":"M",
                "37":"N",
                "36":"O",
                "29":"P",
                "28":"Q",
                "2B":"R",
                "2A":"S",
                "2D":"T",
                "2C":"U",
                "2F":"V",
                "2E":"W",
                "21":"X",
                "20":"Y",
                "23":"Z",
                "18":"a",
                "1B":"b",
                "1A":"c",
                "1D":"d",
                "1C":"e",
                "1F":"f",
                "1E":"g",
                "11":"h",
                "10":"i",
                "13":"j",
                "12":"k",
                "15":"l",
                "14":"m",
                "17":"n",
                "16":"o",
                "09":"p",
                "08":"q",
                "0B":"r",
                "0A":"s",
                "0D":"t",
                "0C":"u",
                "0F":"v",
                "0E":"w",
                "01":"x",
                "00":"y",
                "03":"z",
                "44":"=",
                "57":".",
}

dict_encrypt={v:k for k,v in dict_decrypt.items()}


def decode_string(encoded_string):
 decoded_string="".join([dict_decrypt[encoded_string[i:i+2]] for i in range(0,len(encoded_string),2)])
 return decoded_string

def encode_string(decoded_string):
 encoded_string="".join([dict_encrypt[decoded_string[i]] for i in range(0,len(decoded_string))])
 return encoded_string


def usercustom_decode():
 with open("UserCustom.ini") as fp:
  content=fp.read()
 decoded_content=re.sub(r"\+CVars=(.*)\n",lambda m: "+CVars="+decode_string(m.group(1))+"\n",content)
 with open("UserCustom.ini","w") as fp:
  fp.write(decoded_content)

def usercustom_encode():
 with open("UserCustom.ini") as fp:
  content=fp.read()
 encoded_content=re.sub(r"\+CVars=(.*)\n",lambda m: "+CVars="+encode_string(m.group(1))+"\n",content)
 with open("UserCustom.ini","w") as fp:
  fp.write(encoded_content)
 
 
