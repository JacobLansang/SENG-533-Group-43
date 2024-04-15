import redis
from redis.commands.json.path import Path
from time import time
import traceback
from argparse import ArgumentParser
import psutil

# Resources:
#   https://redis-py.readthedocs.io/en/stable/examples/search_json_examples.html
#   https://redis.io/commands/json.get
#   https://github.com/redis/redis-py/tree/master
#   https://redis.io/docs/data-types/json
#   https://developer.redis.com/howtos/quick-start/cheat-sheet

times_list = []
cpu_usage_list = []
mem_usage_list = []

parser = ArgumentParser()
parser.add_argument('--test', type=int, help='Required positional argument to specify how many tests to run')
args = parser.parse_args()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

if args == None:
    print("ERROR: Test id required")
    exit(1)

# NOTE: LOOPED OUTPUTS ARE QUITE LONG AND MAY CUT OFF OUTPUTS FROM EARLIER TESTS!
try:
    if args.test >= 1:
        # Time to retrieve a clinic
        start_time = time()
        results = r.json().get('clinics-1', '$')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("Test #1:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 2:
        # Time to retrieve all clinics (5 results)
        start_time = time()
        results = r.scan_iter('clinics*')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #2:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # for data in results:
        #     print(r.json().get(data))

    if args.test >= 3:
        # Time to retrieve an owner
        start_time = time()
        results = r.json().get('owners-1', '$')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #3:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 4:
        # Time to retrieve all owners (2000 results)
        start_time = time()
        results = r.scan_iter('owners*')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #4:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # for data in results:
        #     print(r.json().get(data))

    if args.test >= 5:
        # Time to retrieve one pet record
        start_time = time()
        results = r.json().get('petrecords-1', '$')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #5:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 6:
        # Time to retrieve half of all pet records (1000 results)
        start_time = time()
        results = []
        # TODO: See if there are more efficient ways to do this...
        for i, data in enumerate(r.scan_iter('petrecords*')):
            if i > 1000:
                break

            results.append(r.json().get(data, '$'))

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #6:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 7:
        # Time to retrieve all pet records (10000 results)
        start_time = time()
        results = r.scan_iter('petrecords*')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #7:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # for data in results:
        #     print(r.json().get(data))

    if args.test >= 8:
        # Time to retrieve a pet record with PetID=7777
        start_time = time()
        results = r.json().get('petrecords-7777', '$')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #8:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 9:
        # Time to retrieve the address of the clinic associated with the pet record with PetID=7777
        start_time = time()
        clinic_id = r.json().get('petrecords-7777', '$.ClinicID')[0]
        results = r.json().get('clinics-' + str(clinic_id), '$.Address')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #9:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 10:
        # Time to retrieve the surname of the owner associated with the pet record with PetID=7777
        start_time = time()
        owner_id = r.json().get('petrecords-777', '$.OwnerID')[0]
        results = r.json().get('owners-' + str(owner_id), '$.Surname')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #10:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 11:
        # Time to retrieve all pet records who are NOT spayed or neutered (~500 results)
        start_time = time()
        results = []
        for data in r.scan_iter('petrecords*'):
            if r.json().get(data, '$.SpayedOrNeutered')[0] == 'No':
                results.append(r.json().get(data))

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #11:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 12:
        # Time to retrieve all pet records who are cats (~1900 results)
        start_time = time()
        results = []
        for data in r.scan_iter('petrecords*'):
            if r.json().get(data, '$.Animal')[0] == 'Cat':
                results.append(r.json().get(data))

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest 12:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(results)

    if args.test >= 13:
        # Time to retrieve the total amount of fees paid by all owners
        start_time = time()
        total_fees = 0
        for data in r.scan_iter('owners*'):
            total_fees += r.json().get(data, '$.TotalFeesPaid')[0]

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #13:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(total_fees)

    if args.test >= 14:
        # Time to retrieve the average age of all pet records
        start_time = time()
        total_age = 0
        counter = 0
        for data in r.scan_iter('petrecords*'):
            total_age += r.json().get(data, '$.Age')[0]
            counter += 1

        avg_age = total_age / counter

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #14:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(avg_age)

    if args.test >= 15:
        # Time to add a new clinic (ClinicID = 6)
        start_time = time()
        r.json().set('clinics-6', Path.root_path(), {'ClinicID': 6})

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #15:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(r.json().get('clinics-6'))

    if args.test >= 16:
        # Time to add a new owner (OwnerID = 2001)
        start_time = time()
        r.json().set('owners-2001', Path.root_path(), {'OwnerID': 2001})

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #16:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(r.json().get('owners-201'))

    if args.test >= 17:
        # Time to add a new pet record (PetID = 10001)
        start_time = time()
        r.json().set('petrecords-10001', Path.root_path(), {'PetID': 10001})

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest #17:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(r.json().get('petrecords-1001'))

    if args.test >= 18:
        # Time to update a clinic (for ClinicID = 5, NumberOfVets = 9)
        start_time = time()
        r.json().set('clinics-5', '$.NumberOfVets', 9)

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest # 18:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(r.json().get('clinics-5'))

    if args.test >= 19:
        # Time to update an owner (for OwnerID = 2000, Surname = "SMITH")
        start_time = time()
        r.json().set('owners-2000', '$.Surname', 'SMITH')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)

        print("\nTest # 19:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(r.json().get('owners-200'))

    if args.test == 20:
        # Time to update a pet record (for PetID = 10000, Name = "Finnegan")
        start_time = time()
        r.json().set('petrecords-10000', '$.Name', 'Finnegan')

        test_time = time() - start_time
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        times_list.append(test_time)
        cpu_usage_list.append(cpu_usage)
        mem_usage_list.append(mem_usage)
        
        print("\nTest #20:")
        print("  Time: {} ms".format(test_time * 1000))
        print("  CPU Usage: {}".format(cpu_usage))
        print("  Memory Usage: {}".format(mem_usage))
        # print(r.json().get('petrecords-1000'))

    # Printing averages
    print("\n==========\n")
    print("Average time: %.4f ms" % (sum(times_list) / len(times_list)))
    print("Average CPU usage: %.2f %%" % (sum(cpu_usage_list) / len(cpu_usage_list)))
    print("Average memory usage: %.2f %%" % (sum(mem_usage_list) / len(mem_usage_list)))
    print()

except Exception as e:
    print()
    print(traceback.format_exc())

finally:
    # Clean up
    r.delete('clinics-6', 'owners-2001', 'petrecords-10001')
    r.json().set('clinics-5', '$.NumberOfVets', '6')
    r.json().set('owners-2000', '$.Surname', 'BRADLEY')
    r.json().set('petrecords-10000', '$.Name', 'Gretel')
