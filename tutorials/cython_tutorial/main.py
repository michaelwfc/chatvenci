from timeit import timeit
import fib_cython
import external_c_funcs


def run_example():
    import example_cython
    result = example_cython.test(5)
    print(f"result={result}")


if __name__ =="__main__":
    cy_time = timeit(stmt="example_cython.test(100)",setup="import example_cython",number=100)
    py_time = timeit(stmt="example.test(100)",setup="import example",number=100)
    print('cy_time={}\n py_time={}\nCython is {}x faster'.format(cy_time,py_time, py_time/cy_time))

    fib_result = fib_cython.fib(10)
    print(f"fib_result = {fib_result}")

    len_str = external_c_funcs.get_len(str.encode("Hello Cython!"))
    print(f"string length={len_str}")



