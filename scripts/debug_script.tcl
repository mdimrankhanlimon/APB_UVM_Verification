#Open a database for probing HDL signals
database -open waves -into waves.shm -default -event
##or
#database -open -vcd waves -into waves.vcd  -default -gzip

#Probe HDL signals to database for probing
probe -create -all -depth all -memories -dynamic -database waves

#Complete the below probe command to probe the UVM testbench hierarchy, all levels
#ida_probe -wave -wave_probe_args="$uvm:{uvm_test_top} -depth all"
#or
probe -create -database waves uvm_pkg::uvm_top -all -depth all


##Set a breakpoint to stop at the end of the build phase, then run
#uvm_phase -stop_at -build_done
#run

#Complete the command below to enable UVM transaction recording after the build phase completes
uvm_set * recording_detail UVM_FULL


assertion -logging -all -state {failed} -redirect assertion_failed.log
#assertion -logging -all -state {all} -redirect assertion_complete.log
#assertion -summary -byfailure -final -redirect assertion_summary.log
run
exit
