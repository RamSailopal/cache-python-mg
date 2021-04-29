#!/usr/bin/python
import mg_python
mg_python.m_set_host(0, "{{ hst }}", 7041, "", "")
mg_python.m_set_uci(0, "SAMPLES")
result = mg_python.m_get(0, "^Sample.PersonS", 1)
print("The value of subscript 1 in the global Sample.PersonS in the SAMPLES namespace is " + result)
#mg_python.m_release_server_api(0)
