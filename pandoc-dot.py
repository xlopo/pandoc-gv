#!/usr/bin/env python3.3

import json, sys, tempfile, os
from subprocess import Popen, PIPE

tmp_dir = tempfile.mkdtemp(prefix=".tmp_delete_me", dir=".")

def process_dot(obj):

    code_key = u"CodeBlock"
    data = obj.get(code_key, None)

    if not data:
        #print ("Not Codeblock: " + str(obj.keys()))
        code_key=u"Code"
        data = obj.get(code_key, None)

    if not data:
        #print ("Not Code: " + str(obj.keys()))
        return obj

    code_id = data[0][0]

    args = data[0][1]

    if code_id != "gv":
        return obj

    layout = "dot"
    text = data[1]

    if len(args) > 0:
        layout = args[0]

    if layout not in ["dot", "neato", "fdp", "sfdp", "twopi", "circo"]:
        raise(Exception("Unkown layout: \"{}\"".format(layout)))

    #print("==============")
    #print (text)


    gv_command = layout
    p = Popen([gv_command, '-Teps'], stdin=PIPE, stdout=PIPE)
    converted_text = p.communicate(input=text.encode())[0].decode()

    tmp_filename = tempfile.mkstemp(suffix=".eps", prefix="tmp_delete_me_eps_file_", dir=tmp_dir)
    tmp_filename = os.path.relpath(tmp_filename[1])

    f = open(tmp_filename, 'w')
    f.writelines(converted_text)
    f.close()

    tex_command = u"\includegraphics{%s}" %tmp_filename
    p.wait()


    new_obj = {u"RawInline": [u"tex", tex_command] }
    if code_key == u"CodeBlock":
        new_obj = {u"Plain": [new_obj] }

    return new_obj


d = json.load(sys.stdin, object_hook=process_dot)
d = json.dumps(d)

print (d)
