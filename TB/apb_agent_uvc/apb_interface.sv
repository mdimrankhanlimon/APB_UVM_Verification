`include "apb_defines.sv"
`include "uvm_macros.svh"

        import uvm_pkg::* ; 

interface apb_interface (input bit clk);
	
		

   // APB signal interface
    bit                 PCLK_i;
    bit                 PRESETn_i;

    logic[`ADDR_WIDTH-1:0] PADDR_i;
    logic                 PWRITE_i;
    logic[`DATA_WIDTH-1:0] PWDATA_i;
    logic[`BYTE_LANE-1:0]  PSTRB_i;
    logic                 PSEL_i;
    logic                 PENABLE_i;
    logic [`DATA_WIDTH-1:0]PRDATA_o;
    logic                 PREADY_o;
    logic                 PSLVERR_o;

	assign PCLK_i = clk; 


	clocking cb_drvr @(negedge PCLK_i);
		default input #1ps output #1ps;

    	output   PADDR_i;
    	output   PWRITE_i;
    	output   PWDATA_i;
    	output   PSTRB_i;
    	output   PSEL_i;
    	output   PENABLE_i;

    	input  PRDATA_o;
    	input  PREADY_o;
    	input  PSLVERR_o;
	endclocking

	clocking cb_mntr @(posedge PCLK_i);
		default input #1ps output #1ps;

    	input   PADDR_i;
    	input   PWRITE_i;
    	input   PWDATA_i;
    	input   PSTRB_i;
    	input   PSEL_i;
    	input   PENABLE_i;

    	input  PRDATA_o;
    	input  PREADY_o;
    	input  PSLVERR_o;
	endclocking

	modport mp_drvr (
		clocking cb_drvr,
		output PRESETn_i
	);
	
	
	modport mp_mntr (
		clocking cb_mntr,
		input PRESETn_i
	);
/*
	property psel_penable_timing;
	    @(posedge PCLK_i) disable iff(!PRESETn_i) (PSEL_i) |=> $rose(PENABLE_i);
  	endproperty

	assert property (psel_penable_timing)
		else $error("Protocol violation: PENABLE not asserted 1 cycle after PSEL");

	//assert property (psel_penable_timing) `uvm_error(get_name(), "Protocol violation: PENABLE not asserted 1 cycle after PSEL");
*/
endinterface



