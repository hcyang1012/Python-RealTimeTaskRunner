import timeit

def Task_10ms():
    print("Hello#10ms")

def Task_20ms():
    print("Hello#20ms")
    
def Task_100ms():
    print("Hello#100ms")

Tasks = [
    {"Period":10, "Func":Task_10ms, "Counter" : 0},
    {"Period":20, "Func":Task_20ms, "Counter" : 0},
    {"Period":100, "Func":Task_100ms, "Counter" : 0},
]

def run_Task_10ms():
    for Task in Tasks:
        Task["Counter"] += 10
        if Task["Counter"] >= Task["Period"]:
            Task["Counter"] = 0
            Task["Func"]()

start = timeit.default_timer()
while(True):
    end = timeit.default_timer()
    elapsed_ms = int((end - start) * 1000)

    if elapsed_ms > 10:
        run_Task_10ms()
        start = timeit.default_timer()
        