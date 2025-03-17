#!/usr/local/bin/python3

import random

testcase = {}

testcase["sanity_simple_test"] = [
				"owner	:  DVTrainer",
				"run_op : +UVM_TESTNAME=sanity_simple_test",
				"run_op : +UVM_TIMEOUT=500000",
				"run_op : +UVM_VERBOSITY=UVM_LOW"
				"run_op : +BTYE_KNOB=100",
				"cmp_op : +define+ASIC",
				"reg_grp : FULL"
				]

#---------------- Error driving test-----------------------#
testcase["enable_delay_test" ] = [
				"owner	:  Amit",
				"run_op : +UVM_TESTNAME=error_test",
				"run_op : +UVM_TIMEOUT=500000",
				"run_op : +UVM_VERBOSITY=UVM_LOW"
				"run_op : +uvm_set_type_override=apb_driver,sel_enb_error_drive"
				]

testcase["sel_enb_high_together_test"] = [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=error_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_LOW"
		"run_op : +uvm_set_type_override=apb_driver,sel_enb_high_drive"
				]

testcase["enb_high_before_sel_drive_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=error_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_LOW"
		"run_op : +uvm_set_type_override=apb_driver,enb_high_bef_sel_drive"
				]

testcase["enb_high_change_ctrl_drive_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=error_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_LOW"
		"run_op : +uvm_set_type_override=apb_driver,enb_high_change_ctrl_drive"
				]

testcase["enb_low_before_pready_drive_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=error_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_LOW"
		"run_op : +uvm_set_type_override=apb_driver,enb_low_before_pready_drive"
				]

testcase["reset_test"] = [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=reset_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +DEL=5",
				]
#-------------------- Byte_test -------------------------#

testcase["bulk_wr_rd_byte_ALRandSr_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +LOC=ALincr",
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand"  
				]
#-----------------------------------
testcase["cont_wr_rd_byte_ALRandSr_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +LOC=ALincr"
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand"  
				]
testcase["cont_wr_rd_byte_ALRandSr_test_with_randDel"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand"  
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5"
				]
testcase["cont_wr_rd_byte_ALRandSr_test_with_randReset"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1"
				]
testcase["cont_wr_rd_byte_ALRandSr_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand"  
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ] 

testcase["cont_wr_rd_incr_byte_ALRandSr_test"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
        "run_op : +LOC=ALincr"
                ] 
testcase["cont_wr_rd_incr_byte_ALRandSr_test_with_randDel"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5"
                ] 
testcase["cont_wr_rd_incr_byte_ALRandSr_test_with_randReset"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
        "run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1"
                ] 
testcase["cont_wr_rd_incr_byte_ALRandSr_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr ",
        "run_op : +RD_ADDR=incr " ,
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]

testcase["cont_wrIncr_rdDecr_byte_ALRandSr_test"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=decr " , 
        "run_op : +LOC=ALincr"
                ] 
testcase["cont_wrIncr_rdDecr_byte_ALRandSr_test_with_randDel"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr ",
        "run_op : +RD_ADDR=decr " ,
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5"
                ]
testcase["cont_wrIncr_rdDecr_byte_ALRandSr_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr ",
        "run_op : +RD_ADDR=decr " ,
        "run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrIncr_rdDecr_byte_ALRandSr_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr ",
        "run_op : +RD_ADDR=decr " ,
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]

testcase["cont_wrDecr_rdIncr_byte_ALRandSr_test"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=incr " , 
        "run_op : +LOC=ALincr"
                ] 
testcase["cont_wrDecr_rdIncr_byte_ALRandSr_test_with_randDel"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr ",
        "run_op : +RD_ADDR=incr " ,
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5"
                ]
testcase["cont_wrDecr_rdIncr_byte_ALRandSr_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr ",
        "run_op : +RD_ADDR=incr " ,
        "run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrDecr_rdIncr_byte_ALRandSr_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr ",
        "run_op : +RD_ADDR=incr " ,
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]

testcase["cont_wr_rd_decr_byte_ALRandSr_test"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
        "run_op : +LOC=ALincr"
                ] 
testcase["cont_wr_rd_decr_byte_ALRandSr_test_with_randDel"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr ",
        "run_op : +RD_ADDR=decr " ,
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_decr_byte_ALRandSr_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr ",
        "run_op : +RD_ADDR=decr " ,
        "run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wr_rd_decr_byte_ALRandSr_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr ",
        "run_op : +RD_ADDR=decr " ,
        "run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#------------------ Byte_RandL1_test -------------------------------------#


testcase["bulk_wr_rd_byte_RandL1_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +LOC=RandL1",
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand"  
				]

#-------------------------------------------------
testcase["cont_wr_rd_byte_RandL1_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
		"run_op : +LOC=RandL1"
                ]
testcase["cont_wr_rd_byte_RandL1_test_with_randDel"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_byte_RandL1_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1"
                ]
                
testcase["cont_wr_rd_byte_RandL1_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#---------------------------------------------------

#-------------------------------------------------
testcase["cont_wr_rd_incr_byte_RandL1_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1"
				]
testcase["cont_wr_rd_incr_byte_RandL1_test_with_randDel"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_incr_byte_RandL1_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1"
                ]

testcase["cont_wr_rd_incr_byte_RandL1_test_with_randDelReset"] =  [
		"owner	:  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1"
                ]
#----------------------------------------------------------------------

testcase["cont_wrIncr_rdDecr_byte_RandL1_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1"
				]
testcase["cont_wrIncr_rdDecr_byte_RandL1_test_with_randDel"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5"
                ]
testcase["cont_wrIncr_rdDecr_byte_RandL1_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrIncr_rdDecr_byte_RandL1_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#-------------------------------------------------

#-------------------------------------------------
testcase["cont_wrDecr_rdIncr_byte_RandL1_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1"
				]
testcase["cont_wrDecr_rdIncr_byte_RandL1_test_with_randDel"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5"
                ]
testcase["cont_wrDecr_rdIncr_byte_RandL1_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrDecr_rdIncr_byte_RandL1_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#---------------------------------------------------

#--------------------------------------------------
testcase["cont_wr_rd_decr_byte_RandL1_test"] =  [
		"owner	:  Amit",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1"
				]
testcase["cont_wr_rd_decr_byte_RandL1_test_with_randDel"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_decr_byte_RandL1_test_with_randReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wr_rd_decr_byte_RandL1_test_with_randDelReset"] =  [
        "owner  :  Amit",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#----------------------------------------------------------


##################test_start_end_template##################
#----------------c_wr_rd_incr_word_test_start--------------

#----------------c_wr_rd_incr_word_test_end--------------
##########################################################



################--Rashid , Limon--tests--START---############# 
#----------------c_wr_rd_word_test_start------------------

testcase["c_wr_rd_word_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_word_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_word_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_word_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]
#----------------c_wr_rd_word_test_end------------------

#----------------c_wr_rd_incr_word_test_start--------------

testcase["c_wr_rd_incr_word_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_incr_word_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_incr_word_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_incr_word_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------c_wr_rd_incr_word_test_end--------------

#----------------c_wr_rd_decr_word_test_start--------------

testcase["c_wr_rd_decr_word_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_decr_word_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_decr_word_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_decr_word_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------c_wr_rd_decr_word_test_end--------------

#----------------c_wrIncr_rdDecr_word_test_start--------------

testcase["c_wrIncr_rdDecr_word_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_word_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_word_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_word_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]


#----------------c_wrIncr_rdDecr_word_test_end--------------

#----------------c_wrDecr_rdIncr_word_test_start--------------

testcase["c_wrDecr_rdIncr_word_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrDecr_rdIncr_word_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]
testcase["c_wrDecr_rdIncr_word_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1",
        "run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrDecr_rdIncr_word_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------c_wrDecr_rdIncr_word_test_end--------------

#----------------bulk_wr_rd_word_test_start--------------

testcase["bulk_wr_rd_word_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["bulk_wr_rd_word_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]
testcase["bulk_wr_rd_word_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
        "run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["bulk_wr_rd_word_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------bulk_wr_rd_word_test_end--------------

###################################################################

#----------------c_wr_rd_Hword_L1_test_start--------------

testcase["c_wr_rd_Hword_L1_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_Hword_L1_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_Hword_L1_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_Hword_L1_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------c_wr_rd_Hword_L1_test_end--------------

#----------------c_wr_rd_incr_Hword_L1_test_start--------------

testcase["c_wr_rd_incr_Hword_L1_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_incr_Hword_L1_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_incr_Hword_L1_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_incr_Hword_L1_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]
#----------------c_wr_rd_incr_Hword_L1_test_end--------------

#----------------c_wr_rd_decr_Hword_L1_test_start--------------

testcase["c_wr_rd_decr_Hword_L1_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_decr_Hword_L1_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_decr_Hword_L1_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_decr_Hword_L1_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]

#----------------c_wr_rd_decr_Hword_L1_test_end--------------

#----------------c_wrIncr_rdDecr_Hword_L1_test_start--------------

testcase["c_wrIncr_rdDecr_Hword_L1_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_Hword_L1_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_Hword_L1_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_Hword_L1_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]

#----------------c_wrIncr_rdDecr_Hword_L1_test_end--------------

#----------------c_wrDecr_rdIncr_Hword_L1_test_start--------------

testcase["c_wrDecr_rdIncr_Hword_L1_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrDecr_rdIncr_Hword_L1_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrDecr_rdIncr_Hword_L1_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrDecr_rdIncr_Hword_L1_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]

#----------------c_wrDecr_rdIncr_Hword_L1_test_end--------------


#----------------bulk_wr_rd_Hword_L1_test_start--------------

testcase["bulk_wr_rd_Hword_L1_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
        "owner  :  Rashid + Limon"
				]

testcase["bulk_wr_rd_Hword_L1_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]
testcase["bulk_wr_rd_Hword_L1_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
        "run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["bulk_wr_rd_Hword_L1_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=RandL1",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------bulk_wr_rd_Hword_L1_test_end--------------



#######################################################



#----------------c_wr_rd_Hword_BL_test_start--------------

testcase["c_wr_rd_Hword_BL_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_Hword_BL_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_Hword_BL_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_Hword_BL_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------c_wr_rd_Hword_BL_test_end--------------

#----------------c_wr_rd_incr_Hword_BL_test_start--------------

testcase["c_wr_rd_incr_Hword_BL_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=ALincr",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_incr_Hword_BL_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_incr_Hword_BL_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_incr_Hword_BL_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]
#----------------c_wr_rd_incr_Hword_BL_test_end--------------

#----------------c_wr_rd_decr_Hword_BL_test_start--------------

testcase["c_wr_rd_decr_Hword_BL_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=ALincr",
        "owner  :  Rashid + Limon"
				]
testcase["c_wr_rd_decr_Hword_BL_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_decr_Hword_BL_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wr_rd_decr_Hword_BL_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]

#----------------c_wr_rd_decr_Hword_BL_test_end--------------

#----------------c_wrIncr_rdDecr_Hword_BL_test_start--------------

testcase["c_wrIncr_rdDecr_Hword_BL_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr ", 
		"run_op : +RD_ADDR=decr " , 
		"run_op : +LOC=ALincr",
        "owner  :  Rashid + Limon"
				]
testcase["c_wrIncr_rdDecr_Hword_BL_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_Hword_BL_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrIncr_rdDecr_Hword_BL_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]

#----------------c_wrIncr_rdDecr_Hword_BL_test_end--------------

#----------------c_wrDecr_rdIncr_Hword_BL_test_start--------------

testcase["c_wrDecr_rdIncr_Hword_BL_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr " , 
		"run_op : +LOC=ALincr",
        "owner  :  Rashid + Limon"
				]
testcase["c_wrDecr_rdIncr_Hword_BL_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrDecr_rdIncr_Hword_BL_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["c_wrDecr_rdIncr_Hword_BL_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=100",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
                ]

#----------------c_wrDecr_rdIncr_Hword_BL_test_end--------------


#----------------bulk_wr_rd_Hword_BL_test_start--------------

testcase["bulk_wr_rd_Hword_BL_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
        "owner  :  Rashid + Limon"
				]

testcase["bulk_wr_rd_Hword_BL_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "owner  :  Rashid + Limon"
				]
testcase["bulk_wr_rd_Hword_BL_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
        "run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

testcase["bulk_wr_rd_Hword_BL_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  Rashid + Limon"
				]

#----------------bulk_wr_rd_Hword_BL_test_end--------------


#####################----Rashid , limon--END----#######################



#---------------ORTHY-------------------
#----------------c_wr_rd_byte_ALincr_test_------------------

testcase["c_wr_rd_byte_ALIncr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"owner  :  orthy"
				]

testcase["c_wr_rd_byte_ALIncr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"owner  :  orthy"
				]

testcase["c_wr_rd_byte_ALIncr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]

testcase["c_wr_rd_byte_ALIncr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"

				]
#----------------c_wr_rd_byte_ALincr_test_end------------------



#----------------c_wr_rd_incr_byte_ALincr_test_start------------------
testcase["c_wr_rd_incr_byte_ALIncr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"owner  :  orthy"
				]

testcase["c_wr_rd_incr_byte_ALIncr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"owner  :  orthy"
				]

testcase["c_wr_rd_incr_byte_ALIncr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]

testcase["c_wr_rd_incr_byte_ALIncr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]
#----------------c_wr_rd_incr_byte_ALincr_test_end------------------



#----------------c_wr_rd_decr_byte_ALincr_test_start------------------
testcase["c_wr_rd_decr_byte_ALIncr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"owner  :  orthy"
				]

testcase["c_wr_rd_decr_byte_ALIncr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"owner  :  orthy"
				]

testcase["c_wr_rd_decr_byte_ALIncr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]

testcase["c_wr_rd_decr_byte_ALIncr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]
#----------------c_wr_rd_decr_byte_ALincr_test_end------------------



#----------------c_wrIncr_rdDecr_byte_ALincr_test_start------------------
testcase["c_wrIncr_rdDecr_byte_ALIncr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"owner  :  orthy"
				]

testcase["c_wrIncr_rdDecr_byte_ALIncr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"owner  :  orthy"
				]

testcase["c_wrIncr_rdDecr_byte_ALIncr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]

testcase["c_wrIncr_rdDecr_byte_ALIncr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]
#----------------c_wrIncr_rdDecr_byte_ALincr_test_end------------------



#----------------c_wrDecr_rdIncr_byte_ALincr_test_start------------------
testcase["c_wrDecr_rdIncr_byte_ALIncr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"owner  :  orthy"
				]

testcase["c_wrDecr_rdIncr_byte_ALIncr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"owner  :  orthy"
				]

testcase["c_wrDecr_rdIncr_byte_ALIncr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]

testcase["c_wrDecr_rdIncr_byte_ALIncr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]
#----------------c_wrDecr_rdIncr_byte_ALincr_test_end------------------


#----------------bulk_wr_rd_byte_ALincr_test_start--------------

testcase["bulk_wr_rd_byte_ALincr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
        "owner  :  orthy"
				]

testcase["bulk_wr_rd_byte_ALincr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
        "owner  :  orthy"
				]
testcase["bulk_wr_rd_byte_ALincr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
        "run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]

testcase["bulk_wr_rd_byte_ALincr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALincr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  orthy"
				]

#----------------bulk_wr_rd_byte_ALincr_test_end--------------

				

#----------------bappi------------------
#----------------c_wr_rd_byte_ALDecr_test_starts------------------

testcase["c_wr_rd_byte_ALDecr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
		 "owner  :  bappi"
				]
testcase["c_wr_rd_byte_ALDecr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		 "owner  :  bappi"
				]
testcase["c_wr_rd_byte_ALDecr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALdecr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

testcase["c_wr_rd_byte_ALDecr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

#.........
testcase["c_wr_rd_incr_byte_ALDecr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"owner  :  bappi"
				]
testcase["c_wr_rd_incr_byte_ALDecr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"owner  :  bappi"
				]

testcase["c_wr_rd_incr_byte_ALDecr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"

				]

testcase["c_wr_rd_incr_byte_ALDecr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

#..........

testcase["c_wrIncr_rdDecr_byte_ALDecr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
		"owner  :  bappi"
				]
testcase["c_wrIncr_rdDecr_byte_ALDecr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"owner  :  bappi"
				]

testcase["c_wrIncr_rdDecr_byte_ALDecr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"

				]

testcase["c_wrIncr_rdDecr_byte_ALDecr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

#........
testcase["c_wrDecr_rdIncr_byte_ALDecr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"owner  :  bappi"
				]
testcase["c_wrDecr_rdIncr_byte_ALDecr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"owner  :  bappi"
				]
testcase["c_wrDecr_rdIncr_byte_ALDecr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

testcase["c_wrDecr_rdIncr_byte_ALDecr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

#.......

testcase["c_wr_rd_decr_byte_ALDecr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
		"owner  :  bappi"
				]
testcase["c_wr_rd_decr_byte_ALDecr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"owner  :  bappi"
				]
testcase["c_wr_rd_decr_byte_ALDecr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
        "run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

testcase["c_wr_rd_decr_byte_ALDecr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=ALdecr",
    	"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]
#----------------c_wr_rd_knobs_loc_test_end-----------------

#----------------bulk_wr_rd_byte_ALdecr_test_start--------------

testcase["bulk_wr_rd_byte_ALdecr_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALdecr",
        "owner  :  bappi"
				]

testcase["bulk_wr_rd_byte_ALdecr_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
        "owner  :  bappi"
				]
testcase["bulk_wr_rd_byte_ALdecr_reset_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALdecr",
        "run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

testcase["bulk_wr_rd_byte_ALdecr_reset_delay_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=100",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=0", 
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand" , 
		"run_op : +LOC=ALdecr",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1",
        "owner  :  bappi"
				]

#----------------bulk_wr_rd_byte_ALdecr_test_end--------------



##########ATUSHI_test_start####################

#################byte_rand2_start##################

#----------------------------------------------
testcase["bulk_wr_rd_byte_RandL2_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +LOC=RandL2",
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand"  
				]
testcase["bulk_wr_rd_byte_RandL2_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5"
                ]
testcase["bulk_wr_rd_byte_RandL2_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL2",
		"run_op : +RANDOM_RESET=1"
                ]
                
testcase["bulk_wr_rd_byte_RandL2_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]

#------------------------------------------

#-----------------------------------------
testcase["cont_wr_rd_byte_RandL2_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
		"run_op : +LOC=RandL2"
				]
testcase["cont_wr_rd_byte_RandL2_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_byte_RandL2_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL2",
		"run_op : +RANDOM_RESET=1"
                ]
                
testcase["cont_wr_rd_byte_RandL2_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#-------------------------------------------

#-------------------------------------------
testcase["cont_wr_rd_incr_byte_RandL2_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL2"
				]
testcase["cont_wr_rd_incr_byte_RandL2_test_with_randDel"] =  [
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5"
                ]

testcase["cont_wr_rd_incr_byte_RandL2_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL2",
		"run_op : +RANDOM_RESET=1"
                ]


testcase["cont_wr_rd_incr_byte_RandL2_test_with_randDelReset"] =  [
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1"
                ]
#----------------------------------------------------

#----------------------------------------------------
testcase["cont_wrIncr_rdDecr_byte_RandL2_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL2"
				]
testcase["cont_wrIncr_rdDecr_byte_RandL2_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5"
                ]
testcase["cont_wrIncr_rdDecr_byte_RandL2_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL2",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrIncr_rdDecr_byte_RandL2_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#---------------------------------------------------

#---------------------------------------------------
testcase["cont_wrDecr_rdIncr_byte_RandL2_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL2"
				]
testcase["cont_wrDecr_rdIncr_byte_RandL2_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5"
                ]
testcase["cont_wrDecr_rdIncr_byte_RandL2_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL2",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrDecr_rdIncr_byte_RandL2_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#------------------------------------------------------

#------------------------------------------------------
testcase["cont_wr_rd_decr_byte_RandL2_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL2"
				]
testcase["cont_wr_rd_decr_byte_RandL2_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_decr_byte_RandL2_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL2",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wr_rd_decr_byte_RandL2_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL2",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#-----------------------------------------------------------
#################byte_rand2_end##################



################byte_rand3_start#################

#-------------------------------------------------------
testcase["bulk_wr_rd_byte_RandL3_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +LOC=RandL3",
		"run_op : +WR_ADDR=rand", 
		"run_op : +RD_ADDR=rand"  
				]
testcase["bulk_wr_rd_byte_RandL3_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5"
                ]
testcase["bulk_wr_rd_byte_RandL3_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL3",
		"run_op : +RANDOM_RESET=1"
                ]
                
testcase["bulk_wr_rd_byte_RandL3_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]

#------------------------------------------------------

#------------------------------------------------------
testcase["cont_wr_rd_byte_RandL3_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
		"run_op : +LOC=RandL3"
				]
testcase["cont_wr_rd_byte_RandL3_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_byte_RandL3_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL3",
		"run_op : +RANDOM_RESET=1"
                ]
                
testcase["cont_wr_rd_byte_RandL3_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=rand",
        "run_op : +RD_ADDR=rand" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#--------------------------------------------------------

#--------------------------------------------------------
testcase["cont_wr_rd_incr_byte_RandL3_test"] =  [
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL3"
				]
testcase["cont_wr_rd_incr_byte_RandL3_test_with_randDel"] =  [
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5"
                ]

testcase["cont_wr_rd_incr_byte_RandL3_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL3",
		"run_op : +RANDOM_RESET=1"
                ]


testcase["cont_wr_rd_incr_byte_RandL3_test_with_randDelReset"] =  [
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5",
		"run_op : +RANDOM_RESET=1"
                ]
#--------------------------------------------------------

#--------------------------------------------------------
testcase["cont_wrIncr_rdDecr_byte_RandL3_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=incr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL3"
				]
testcase["cont_wrIncr_rdDecr_byte_RandL3_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5"
                ]
testcase["cont_wrIncr_rdDecr_byte_RandL3_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL3",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrIncr_rdDecr_byte_RandL3_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=incr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#------------------------------------------------------

#------------------------------------------------------
testcase["cont_wrDecr_rdIncr_byte_RandL3_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=incr" , 
		"run_op : +LOC=RandL3"
				]
testcase["cont_wrDecr_rdIncr_byte_RandL3_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5"
                ]
testcase["cont_wrDecr_rdIncr_byte_RandL3_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL3",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wrDecr_rdIncr_byte_RandL3_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=incr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#--------------------------------------------------------

#--------------------------------------------------------
testcase["cont_wr_rd_decr_byte_RandL3_test"] =  [
		"owner	:  Atushi",
		"run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
		"run_op : +UVM_TIMEOUT=500000",
		"run_op : +UVM_VERBOSITY=UVM_HIGH",
		"run_op : +WORD_KNOB=0",
		"run_op : +HALF_WORD_KNOB=0",
		"run_op : +BYTE_KNOB=100", 
		"run_op : +WR_ADDR=decr", 
		"run_op : +RD_ADDR=decr" , 
		"run_op : +LOC=RandL3"
				]
testcase["cont_wr_rd_decr_byte_RandL3_test_with_randDel"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5"
                ]
testcase["cont_wr_rd_decr_byte_RandL3_test_with_randReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL3",
		"run_op : +RANDOM_RESET=1"
                ]
testcase["cont_wr_rd_decr_byte_RandL3_test_with_randDelReset"] =  [
        "owner  :  Atushi",
        "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
        "run_op : +UVM_TIMEOUT=500000",
        "run_op : +UVM_VERBOSITY=UVM_HIGH",
        "run_op : +WORD_KNOB=0",
        "run_op : +HALF_WORD_KNOB=0",
        "run_op : +BYTE_KNOB=100",
        "run_op : +WR_ADDR=decr",
        "run_op : +RD_ADDR=decr" ,
        "run_op : +LOC=RandL3",
		"run_op : +DEL=5",
        "run_op : +RANDOM_RESET=1"
                ]
#-------------------------------------------

###############byte_rand3_end####################

###########---ATUSHI_test_end---####################

for i in range(1,225):
    knob_1 = random.randint(0, 100)
    knob_2 = random.randint(0, 100)
    knob_3 = random.randint(0, 100)
    depth_val = random.choice([512, 1024, 2048, 4096, 8192])

    testcase["all_random_test_"+str(i)] = [
             "owner  :  Rashid",
             "cmp_op : -define DEPTH="+str(depth_val),
             "run_op : +UVM_TESTNAME=c_wr_rd_knobs_loc_test",
             "run_op : +UVM_TIMEOUT=500000",
             "run_op : +UVM_VERBOSITY=UVM_HIGH",
             "run_op : +WORD_KNOB="+str(knob_1),                
             "run_op : +HALF_WORD_KNOB="+str(knob_2),
             "run_op : +BYTE_KNOB="+str(knob_3),
             "run_op : +WR_ADDR="+str(random.choice(['incr', 'decr', 'rand'])),
             "run_op : +RD_ADDR="+str(random.choice(['incr', 'decr', 'rand'])),
             "run_op : +LOC="+str(random.choice(['ALincr', 'ALdecr', 'RandL1','RandL2','RandL3']))
                      ]

