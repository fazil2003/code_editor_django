from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def code_python(request):
    return render(request,"python.html")

def run_python(request):
    if request.method =='POST':
        code=request.POST['code']
        with open("filename.py","w") as f:
             f.writelines(code)

        # exec(open("filename.py").read())
        

        # #### Code to Run python Script ###
        import sys
        from io import StringIO
        import contextlib

        @contextlib.contextmanager
        def stdoutIO(stdout=None):
            old = sys.stdout
            if stdout is None:
                stdout = StringIO()
            sys.stdout = stdout
            yield stdout
            sys.stdout = old

        with stdoutIO() as s:
            #exec(code)
            exec(open("filename.py").read())

        return HttpResponse(s.getvalue())


def code_c(request):
    return render(request,"c.html")

def run_c(request):
    if request.method =='POST':
        code=request.POST['code']
        with open('hello_world.c','w') as f:
            f.write(code)
        import subprocess
        
        s=subprocess.check_call("gcc hello_world.c -o out1;./out1", shell = True) 
        proc = subprocess.Popen("gcc hello_world.c -o out1;./out1", stdout=subprocess.PIPE,shell=True)
        output = proc.stdout.read()


        return HttpResponse(output)

def code_cpp(request):
    return render(request,"cpp.html")

def run_cpp(request):
    if request.method =='POST':
        code=request.POST['code']
        with open('hello_world.cpp','w') as f:
            f.write(code)
        import subprocess
        
        s=subprocess.check_call("g++ hello_world.cpp -o out2;./out2", shell = True) 
        proc = subprocess.Popen("g++ hello_world.cpp -o out2;./out2", stdout=subprocess.PIPE,shell=True)
        output = proc.stdout.read()


        return HttpResponse(output)

def load(request):
    if request.method =='POST':
        code=request.POST['code']

        # #### Code to Run python Script ###
        # import sys
        # from io import StringIO
        # import contextlib

        # @contextlib.contextmanager
        # def stdoutIO(stdout=None):
        #     old = sys.stdout
        #     if stdout is None:
        #         stdout = StringIO()
        #     sys.stdout = stdout
        #     yield stdout
        #     sys.stdout = old

        # with stdoutIO() as s:
        #     exec(code)

        # return HttpResponse(s.getvalue())
        # gcc code_files/hello_world.c -o code_files/out1;code_files/out1



        ### Code to Run C Program ###

        with open('hello_world.c','w') as f:
            f.write(code)
        import subprocess
        
        s=subprocess.check_call("gcc hello_world.c -o out1;./out1", shell = True) 
        proc = subprocess.Popen("gcc hello_world.c -o out1;./out1", stdout=subprocess.PIPE,shell=True)
        output = proc.stdout.read()


        return HttpResponse(output)

def editor_python(request):
    return render(request,"python_editor.html")

def editor_c(request):
    return render(request,"c_editor.html")

def editor_cpp(request):
    return render(request,"cpp_editor.html")
        

        