import time

# 1. Current time in seconds since epoch
print("\ntime():", time.time())

# 2. Sleep for 3 second
print("\nSleeping for 3 second...")
time.sleep(3)

# 3. Human-readable string of current time
print("\nctime():", time.ctime())

# 4. Local time tuple
print("\nlocaltime():", time.localtime())

# 5. UTC time tuple
print("\ngmtime():", time.gmtime())

# 6. Convert local time tuple → seconds
lt = time.localtime()
print("\nmktime(localtime):", time.mktime(lt))

# 7. Format time tuple → string
print("\nstrftime:", time.strftime("%Y-%m-%d %H:%M:%S", lt))

# 8. Parse string → time tuple
parsed = time.strptime("2026-07-03", "%Y-%m-%d")
print("\nstrptime:", parsed)

# 9. High-precision performance counter
start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()
print("\nperf_counter (elapsed):", end - start)

# 10. Monotonic clock
print("\nmonotonic():", time.monotonic())

# 11. CPU process time
print("\nprocess_time():", time.process_time())

# 12. Convert tuple → readable string
print("\nasctime():", time.asctime())

# (Unix-specific functions, may not work on Windows)
try:
    print("\nclock_gettime(CLOCK_REALTIME):", time.clock_gettime(time.CLOCK_REALTIME))
    print("\nclock_getres(CLOCK_REALTIME):", time.clock_getres(time.CLOCK_REALTIME))
except AttributeError:
    print("\nclock_gettime/clock_getres not available on this OS")
