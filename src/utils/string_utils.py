
import base64
from typing import Text


def encoding_string_to_base64_string(s:Text="GeeksForGeeks is the best",encording="utf-8" ):
    # utf_bytes = bytes(s,"utf-8")
    s_bytes = s.encode(encording)
    base64_bytes = base64.b64encode(s_bytes) 
    base64_string = base64_bytes.decode(encording)
    return base64_string


def decoding_base64_string_to_string(base64_string =" R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA ==",encording="utf-8" ):
    base64_bytes = base64_string.encode(encording) 
    string_bytes = base64.b64decode(base64_bytes) 
    string = string_bytes.decode(encording) 
    return string