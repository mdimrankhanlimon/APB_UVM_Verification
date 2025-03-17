TEST_NAME = base_test

vcmp:
	@rm -rf $(TEST_NAME)
	@mkdir $(TEST_NAME)
	#@xvlog -f ./rtl_files.f ./tb_files.f -sv -L uvm --log ./$(TEST_NAME)/rtl_compilation.log
	#@xvlog -f ./tb_files.f -sv -L uvm --log ./$(TEST_NAME)/tb_compilation.log
	@xvlog -f ./rtl_files.f --log ./$(TEST_NAME)/rtl_compilation.log
	@xvlog -sv ./tb_files.sv -L uvm --log ./$(TEST_NAME)/tb_compilation.log

velb: cmp
	@xelab -timescale 1ns/1ps -debug all -top tb_top -s tb_top_snap -L uvm --log ./$(TEST_NAME)/elaboration.log

vsim: elb
	@xsim tb_top_snap -R -testplusarg UVM_TESTNAME=$(TEST_NAME) -sv_seed  100 -testplusarg UVM_TIMEOUT=1us --log ./$(TEST_NAME)/run_simulation.log
	#@mv dump.vcd ./$(TEST_NAME)/
	#@xsim tb_top_snap -R -testplusarg UVM_TESTNAME=$(TEST_NAME) -sv_seed  100 -testplusarg UVM_TIMEOUT=1us --log ./$(TEST_NAME)/run_simulation.log -testplusarg DUMP

vwave: sim dump.vcd
	@gtkwave dump.vcd &

WORD_KNOB = 100
HALF_WORD_KNOB = 0
BYTE_KNOB = 0
WR_ADDR =
RD_ADDR =
LOC = 

cln:
	rm -rf *.log  *.pb *.jou xsim.dir *.wdb xrun* xcelium.d
	reset
	@ls -ltrh

RANDOM_RESET = 0
DEL = 0
ERR = sel_enb_error_drive 
#sel_enb_error_drive sel_enb_high_drive enb_high_bef_sel_drive enb_high_change_ctrl_drive enb_low_before_pready_drive

xelb: 
	@xrun \
			-access +rwc \
			-timescale 1ns/1ps \
			-sv -sysv \
			-incdir ../RTL/ -f rtl_files.f -incdir ../TB/ -f tb_files.f \
			-uvm -uvmhome /home/cadence_install/xcelium/tools/methodology/UVM/CDNS-1.2 \
			-define cdnc +fsmdebug \
			-snapshot tb_top_snap -createdebugdb \
			-elaborate

xsim: 
	@xrun \
			-r tb_top_snap \
			+UVM_TESTNAME=$(TEST_NAME) \
			+UVM_TIMEOUT=8000000 +UVM_VERBOSITY=UVM_HIGH \
			+WORD_KNOB=$(WORD_KNOB) \
			+HALF_WORD_KNOB=$(HALF_WORD_KNOB) \
			+BYTE_KNOB=$(BYTE_KNOB) \
			+WR_ADDR=$(WR_ADDR) \
			+RD_ADDR=$(RD_ADDR) \
			+LOC=$(LOC) \
			+DEL=$(DEL) \
			+RANDOM_RESET=$(RANDOM_RESET)

			#+uvm_set_type_override=apb_driver,$(ERR)
			#@mv dump.vcd ./$(TEST_NAME)/

xdbg: 
	@xrun \
			-r tb_top_snap \
			+UVM_TESTNAME=$(TEST_NAME) \
			+UVM_TIMEOUT=80000 +UVM_VERBOSITY=UVM_LOW -input debug_script.tcl
			#@mv dump.vcd ./$(TEST_NAME)/

xwave: dump.vcd
	@simvision dump.vcd &

hcln:
	rm -rf *.log  *.pb *.jou xsim.dir *.wdb xrun* xcelium.d dump* waves*
	rm -rf *log
	rm -rf x*
	reset
	@ls -ltrh

