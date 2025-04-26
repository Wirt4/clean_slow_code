# clean_slow_code
 credit to YouTube channel "Molly Rocket" for demonstrating these comparisons

 Running for benchmarks
 ```
 python -m timeit -n 100 -r 1 -s "from clean import create_shapes, compute_total_area; shapes = create_shapes()" "compute_total_area(shapes)"
python -m timeit -n 100 -r 1 -s "from demo import create_shapes, compute_total_area; shapes = create_shapes()" "compute_total_area(shapes)"
```