#!/usr/local/bin/python3
from test_list import *
import re
import subprocess
import os
import shutil
import glob
import argparse
import time  
import random
from datetime import datetime

#--------------------------------------
#  User Variable Section
#--------------------------------------
elab_cmd_xrun = "xrun -access +rwc -timescale 1ns/1ps -sv -sysv -f rtl_files.f -f tb_files.f -uvm -uvmhome /home/cadence_install/xcelium/tools/methodology/UVM/CDNS-1.2 +fsmdebug -snapshot tb_top_snap >> flow_logfile.txt  -createdebugdb -elaborate -log ./elaborate/run_elaboration.log "

run_cmd_xrun = "xrun -r tb_top_snap >> flow_logfile.txt "
#run_cmd_xrun = "xrun -r tb_top_snap "

debug_cmd_xrun = "xrun -access +rwc -timescale 1ns/1ps -sv -sysv -f rtl_files.f  -f tb_files.f -uvm -uvmhome /home/cadence_install/xcelium/tools/methodology/UVM/CDNS-1.2 +fsmdebug -snapshot tb_top_snap >> flow_logfile.txt -createdebugdb -input debug_script.tcl"

#debug_cmd_xrun = "xrun -access +rwc -timescale 1ns/1ps -sv -sysv -f rtl_files.f  -f tb_files.f -uvm -uvmhome /home/cadence/cadence_installs/Xcelium/tools.lnx86/methodology/UVM/CDNS-1.2 +fsmdebug -snapshot tb_top_snap -createdebugdb -input debug_script.tcl"
elab_and_run_xrun = "xrun -access +rwc -timescale 1ns/1ps -sv -sysv -f rtl_files.f -f tb_files.f -uvm -uvmhome /home/cadence_install/xcelium/tools/methodology/UVM/CDNS-1.2 +fsmdebug -snapshot tb_top_snap >> flow_logfile.txt -createdebugdb -run"

#--------------------------------------
#  Script Variable Section
#--------------------------------------
my_list = []
elab_then_run = []
no_need_elab_only_run = []
run_cmn_elab = []
my_final_cmd = ""
successful_tests = 0
unsuccessful_tests = 0
pass_count = 0
fail_count = 0
fatal_count =0
start_time=0
end_time=0
#--------------------------------------

def get_run_op(my_test):
    my_list.clear()
    new_str = ""
    for op in my_test:
        if "run_op" in op:
            new_str = string_regexp(op, "run_op", new_str)
            my_list.append(op)
    return new_str

def get_cmp_op(my_test):
    my_list.clear()
    new_str = ""
    for op in my_test:
        if "cmp_op" in op:
            new_str = string_regexp(op, "cmp_op", new_str)
            my_list.append(op)
    return new_str

def get_reg_grp(my_test):
    my_list.clear()
    new_str = ""
    for op in my_test:
        if "reg_grp" in op:
            new_str = string_regexp(op, "reg_grp", new_str)
            my_list.append(op)
    return new_str

def get_data_dic(my_dict, my_test, op_type):
    if my_dict.get(my_test):
        if op_type == "run_op":
            return get_run_op(my_dict[my_test])
        elif op_type == "cmp_op":
            return get_cmp_op(my_dict[my_test])
        elif op_type == "reg_grp":
            return get_reg_grp(my_dict[my_test])
        elif op_type == "all":
            return (my_dict[my_test])
    else:
        print(f"No test available named {my_test} in {type(my_dict)} list")
        exit()

def string_regexp(hndl, pattern, my_str):
    if pattern == "run_op":
        match = re.match(r"run_op.*:(.*)", hndl)
    elif pattern == "cmp_op":
        match = re.match(r"cmp_op.*:(.*)", hndl)
    elif pattern == "reg_grp":
        match = re.match(r"reg_grp.*:(.*)", hndl)

    if match:
        my_str = my_str + " " + match.group(1)
    return my_str
'''
##..............................
#      Command Generation --- this function is not used 
##..............................
def command_gen(my_dict, my_test, seed_value):
    my_elb = get_data_dic(my_dict, my_test, "cmp_op")
    my_run = get_data_dic(my_dict, my_test, "run_op")
    my_final_cmd = ""
    
    if len(my_elb) > 2:
        #my_final_cmd = f"{elab_and_run_xrun} -svseed {seed_value} {my_elb} {my_run}"
        my_final_cmd = f"{elab_and_run_xrun} {my_elb} {my_run}"
        elab_then_run.append(my_final_cmd)
    else:
        #my_final_cmd = f"{run_cmd_xrun} -svseed {seed_value} {my_run}"
        my_final_cmd = f"{run_cmd_xrun} {my_run}"
        no_need_elab_only_run.append(my_final_cmd)
'''
##............time....................
def format_time(timestamp):
    """Format a timestamp to a human-readable string."""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

##....................................
##    Function for regression run
##....................................
def regression_gen(my_dict,seed_value,verbosity):
    global successful_tests
    global pass_count
    global fail_count
    test_list = list(my_dict.keys())
    timestamp = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())

    for my_test in test_list:
        
        start_time = time.time()  # Start time
        start_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"Test '{my_test}'\n\t|| Start: {start_time_str} ")

        my_elb = get_data_dic(my_dict, my_test, "cmp_op")
        my_run = get_data_dic(my_dict, my_test, "run_op")
        my_final_cmd = ""

        if len(my_elb) > 2:
            my_final_cmd = f"{elab_and_run_xrun} -svseed {seed_value} +UVM_VERBOSITY={verbosity} {my_elb} {my_run}"

            if os.path.exists(my_test):
                shutil.rmtree(my_test)
            #os.mkdir(my_test)

            if not os.path.exists("./elaborate/tb_top_snap"):
                xelb()

            result = subprocess.run(
                f"{my_final_cmd} -log ./{timestamp}_regr/{my_test}/{my_test}_run_simulation.log",
                shell=True
            )

        else:
            my_final_cmd = f"{run_cmd_xrun} {my_run} -svseed {seed_value} +UVM_VERBOSITY={verbosity} "

            if os.path.exists(my_test):
                shutil.rmtree(my_test)
            #os.mkdir(my_test)

            if not os.path.exists("./elaborate/tb_top_snap"):
                xelb()

            result = subprocess.run(
                f"{my_final_cmd} -log ./{timestamp}_regr/{my_test}/{my_test}_run_simulation.log",
                shell=True
            )

        if result.returncode == 0:
            successful_tests += 1
        if result.returncode == 1:
            successful_tests += 1
            print(f"{my_test} is unsuccessful")

        if os.path.exists("dump.vcd"):
            os.remove("dump.vcd")
        if os.path.exists("waves.shm"):
            shutil.move("waves.shm", f"./{timestamp}_regr/{my_test}/")
        if os.path.exists("apb_monitor.log"):
            shutil.move("apb_monitor.log", f"./{timestamp}_regr/{my_test}/")

        end_time = time.time()  # End time
        duration = end_time - start_time  # Duration
        end_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))

        print(f"\t|| End: {end_time_str} || Duration: {duration:.2f} seconds \n")
        
        test_pass_fail(f"./{timestamp}_regr/{my_test}/{my_test}_run_simulation.log")

##..................................................
#...............single test run.....................
##..................................................

def single_run(my_dict, my_test, seed_value, verbosity):
    global successful_tests
    global pass_count
    global fail_count
    test_list = list(my_dict.keys())
    
    timestamp = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    start_time = time.time()  # Start time
    start_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
    print(f"Test '{my_test}'\n\t|| Start: {start_time_str} ")

    my_elb = get_data_dic(my_dict, my_test, "cmp_op")
    my_run = get_data_dic(my_dict, my_test, "run_op")
    my_final_cmd = ""

    if len(my_elb) > 2:
        my_final_cmd = f"{elab_and_run_xrun} -svseed {seed_value} +UVM_VERBOSITY={verbosity} {my_elb} {my_run}"

        if os.path.exists(my_test):
            shutil.rmtree(my_test)
        #os.mkdir(my_test)

        result = subprocess.run(
            f"{my_final_cmd} -log ./{timestamp}_single_test_run/{my_test}/{my_test}_run_simulation.log",
            shell=True
        )

    else:
        my_final_cmd = f"{run_cmd_xrun} {my_run} +UVM_VERBOSITY={verbosity} -svseed {seed_value}"

        if os.path.exists(my_test):
            shutil.rmtree(my_test)
        #os.mkdir(my_test)

        result = subprocess.run(
            f"{my_final_cmd} -log ./{timestamp}_single_test_run/{my_test}/{my_test}_run_simulation.log",
            shell=True
        )

    if result.returncode == 0:
        successful_tests += 1
    if result.returncode == 1:
        unsuccessful_tests += 1
        print(f"{my_test} is unsuccessful")

    if os.path.exists("dump.vcd"):
        shutil.move("dump.vcd", f"./{timestamp}_single_test_run/{my_test}/")
    if os.path.exists("waves.shm"):
        shutil.move("waves.shm", f"./{timestamp}_single_test_run/{my_test}/")
    if os.path.exists("apb_monitor.log"):
        shutil.move("apb_monitor.log", f"./{timestamp}_single_test_run/{my_test}/")

    end_time = time.time()  # End time
    duration = end_time - start_time  # Duration
    end_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))

    print(f"\t|| End: {end_time_str} || Duration: {duration:.2f} seconds \n")

    test_pass_fail(f"./{timestamp}_single_test_run/{my_test}/{my_test}_run_simulation.log")

##..................................................
#............... debug test run .....................
##..................................................

def single_run_with_debug(my_dict, my_test, seed_value, verbosity):
    global successful_tests
    global pass_count
    global fail_count
    test_list = list(my_dict.keys())
    
    timestamp = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    start_time = time.time()  # Start time
    start_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
    print(f"Test '{my_test}'\n\t|| Start: {start_time_str} ")

    my_elb = get_data_dic(my_dict, my_test, "cmp_op")
    my_run = get_data_dic(my_dict, my_test, "run_op")
    my_final_cmd = ""

    my_final_cmd = f"{debug_cmd_xrun} -svseed {seed_value} +UVM_VERBOSITY={verbosity} {my_elb} {my_run}"

    if os.path.exists(my_test):
       shutil.rmtree(my_test)

    result = subprocess.run(
            f"{my_final_cmd} -log ./{timestamp}_single_test_run/{my_test}/{my_test}_run_simulation.log",
            shell=True
        )

    if result.returncode == 0:
        successful_tests += 1
    if result.returncode == 1:
        successful_tests += 1
        print(f"{my_test} is unsuccessful")

    if os.path.exists("dump.vcd"):
        shutil.move("dump.vcd", f"./{timestamp}_single_test_run/{my_test}/")
    if os.path.exists("waves.shm"):
        shutil.move("waves.shm", f"./{timestamp}_single_test_run/{my_test}/")
    if os.path.exists("apb_monitor.log"):
        shutil.move("apb_monitor.log", f"./{timestamp}_single_test_run/{my_test}/")

    end_time = time.time()  # End time
    duration = end_time - start_time  # Duration
    end_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))

    print(f"\t|| End: {end_time_str} || Duration: {duration:.2f} seconds \n")

    test_pass_fail(f"./{timestamp}_single_test_run/{my_test}/{my_test}_run_simulation.log")

##...........................................
#..............elaboration...................
##...........................................

def xelb():
    '''
    cmd = (
        "xrun -elaborate -access +rwc -timescale 1ns/1ps -f ./rtl_files.f -f ./tb_files.f -uvm "
        "-uvmhome /home/cadence/cadence_installs/Xcelium/tools.lnx86/methodology/UVM/CDNS-1.2 "
        "-define cdnc +fsmdebug -snapshot tb_top_snap -createdebugdb -log ./elaborate/run_elaboration.log "
    )'''
    subprocess.run(elab_cmd_xrun, shell=True)
##...........................................
#..............cleaning function.............
##...........................................

def clean_and_list():
    files_to_delete = ["*.log", "*.pb", "*.jou", "*.wdb", "dump*", "*.diag"]
    dirs_to_delete = ["xsim.dir", "xcelium.d", "waves.shm", "elaborate*"]
    for file_pattern in files_to_delete:
        for file_path in glob.glob(file_pattern):
            os.remove(file_path)
    for dir_to_delete in dirs_to_delete:
        shutil.rmtree(dir_to_delete, ignore_errors=True)
    subprocess.run(["reset"])
    subprocess.run(["ls", "-ltrh"])

#...........................................
##............test_pass_fail................
#...........................................
def test_pass_fail(logfile_path):
    global pass_count
    global fail_count
    global fatal_count

    # Check if the log file exists
    if not os.path.exists(logfile_path):
        print(f"The log file {logfile_path} does not exist.")
        return pass_count, fail_count, fatal_count

    # Initialize variables
    found_uvm_fatal = False

    # Open and read the log file
    with open(logfile_path, "r") as logfile:
        for line in logfile:
            if "TEST PASS" in line:
                pass_count += 1
            elif "TEST FAIL" in line:
                fail_count += 1
                print(f"\tFAIL in {logfile_path}")
            elif "UVM_FATAL :" in line:
                # Extract the number after "UVM_FATAL :"
                fatal_value = int(line.split(":")[1].strip())
                found_uvm_fatal = True

                # If UVM_FATAL is not 0, increase fatal_count
                if fatal_value != 0:
                    fatal_count += 1
                    print(f"\tFATAL ERROR in {logfile_path}")

    # Return the updated counts
    return pass_count, fail_count, fatal_count

#..........................................
#.............vivado.......................
#..........................................
def vcmp():
    subprocess.run(["bash", "-c", f"xvlog -f ./rtl_files.f --log ./{test_name}/rtl_compilation.log"])
    subprocess.run(["bash", "-c", f"xvlog -sv ./tb_files.sv -L uvm --log ./{test_name}/tb_compilation.log"])

def velb():
    vcmp()  # Call vcmp here to compile before elaboration
    subprocess.run(["bash", "-c", f"xelab -timescale 1ns/1ps -debug all -top tb_top -s tb_top_snap -L uvm"])

def vsim(test_name):
    if os.path.exists(test_name):
        shutil.rmtree(test_name)
    os.mkdir(test_name)
    velb(test_name)  # Call velb here to compile and elaborate before simulation
    subprocess.run(["bash", "-c", f"xsim tb_top_snap -R -testplusarg UVM_TESTNAME={test_name} -sv_seed 100 -testplusarg UVM_TIMEOUT=1us --log ./{test_name}/run_simulation.log"])
    if os.path.exists("dump.vcd"):
        shutil.move("dump.vcd", f"./{test_name}/")

##...........................................
#..............custom help function..........
##...........................................

def custom_help():
    print('\n')
    print('Custom help message:')
    print('\n')
    print('Switches:')
    print('    --test: Test name (default: sanity_test)')
    print('    --run: Run type (choices: cmp, elb, sim, wave; default: sim)')
    print('    --tool: Tool name (choices: vivado, xlim; default: vivado)')
    print('    --seed: Seed value for the simulation, default value ==0')
    print('    --verbosity: UVM verbosity for the simulation, default value ==UVM_NONE')
    print('    --regr: Run regression test')
    print('    --remove: Remove all directories existing in the current directory')
    print('    --help: Show this custom help message')
    print('\n')
    print('sample command for Elaboration:\n \t ./run_script.py --run elb --tool xlim')
    print('\n')
    print('sample command for single test:\n \t ./run_script.py --test sanity_test --run sim --tool xlim --seed 12345')
    print('\n')
    print('command for regression:\n \t ./run_script.py --regr --seed 125')
    print('\n')




def remove():
    subprocess.run(["find", ".", "-type", "d", "-name", "*test*", "-exec", "rm", "-r", "{}", "+"])
    files_to_delete = ["*.log", "*.pb", "*.jou", "*.wdb", "dump*", "*.diag", "*.history", "*.txt"]
    dirs_to_delete = ["xsim.dir", "xcelium.d", "waves.shm", "elaborate", "__pycache__"]
    for file_pattern in files_to_delete:
        for file_path in glob.glob(file_pattern):
            os.remove(file_path)
    for dir_to_delete in dirs_to_delete:
        shutil.rmtree(dir_to_delete, ignore_errors=True)
    subprocess.run(["reset"])
    subprocess.run(["ls", "-ltrh"])

def test_pass_fail_count():
    print("\n Test Completed")
    print(f"\t Number of Successful Tests Simulated: {successful_tests}")
    #print(f"\t Number of Unsuccessful Tests: {unsuccessful_tests}")
    print(f"\t Number of TEST PASS: {pass_count}")
    print(f"\t Number of TEST FAIL: {fail_count}")
    print(f"\t Number of TEST FATAL: {fatal_count}")
    if successful_tests > 0:
        print(f"\t Number of Passing Rate: {(pass_count/successful_tests)*100}%")
    else:
        print("\t No Test is Successful")



##...........................................
#..............main function.................
##...........................................
def main():
    global successful_tests
    global unsuccessful_tests
    try:
        parser = argparse.ArgumentParser(description='Run simulation scripts.', add_help=False)
        parser.add_argument('--test', default='sanity_test', help='Test name (default: sanity_test)')
        parser.add_argument('--run', default='sim', choices=['cmp', 'elb', 'sim', 'debug'], help='Run type (default: sim)')
        parser.add_argument('--tool', default='xlim', choices=['vivado', 'xlim'], help='Tool name (default: vivado)')
        parser.add_argument('--seed', default=int(time.time()), type=int, help='Seed value for the simulation (default: current time)')
        parser.add_argument('--regr', action='store_true', help='Run regression test')
        parser.add_argument('--verbosity', default='UVM_NONE', choices=['UVM_NONE', 'UVM_LOW','UVM_MEDIUM','UVM_HIGH','UVM_DEBUG'], help='Tool name (default: vivado)')
        parser.add_argument('--help', action='store_true', help='Show custom help message')
        parser.add_argument('--remove', action='store_true', help='Remove previous simulation data')

        args = parser.parse_args()

        if args.help:
            custom_help()
            return
        if args.remove:
            remove()
            return
        
        my_test = args.test
        run = args.run
        tool = args.tool
        seed_value = args.seed
        verbosity = args.verbosity

        if run == "cmp":
            if tool == "vivado":
                vcmp(my_test)
            elif tool == "xlim":
                xcmp(my_test)
        elif run == "elb":
            if tool == "vivado":
                velb()
            elif tool == "xlim":
                print("Elaboration Started")
                xelb()
                print("Elaboration is done")
        elif run == "sim":
            if args.regr:
                regression_gen(testcase, seed_value, verbosity)  # my_dict == testcase
                test_pass_fail_count()
            elif tool == "xlim":
                single_run(testcase, my_test, seed_value,verbosity)
                test_pass_fail_count()
            elif tool == "vivado":
                vsim(my_test)
                test_pass_fail_count()
        elif run == "debug":
            if tool == "xlim":
                single_run_with_debug(testcase, my_test, seed_value,verbosity)
                test_pass_fail_count()
            elif tool == "vivado":
                print("This feature is not available for vivado tool")
        elif run == "wave":
            wave()
    except SystemExit as error:
        if error.code != 0:
            custom_help()

if __name__ == "__main__":
    main()

