/***************************************************************
*
*
*
************************************************************/

`include "clock_gen.sv"

module tb_top;
	`include "uvm_macros.svh"
	import uvm_pkg::* ;
	import top_pkg::* ;


	// signal defination
	bit clk_out;

	// clock generation
	clock_gen clk_gen(clk_out);

	// interface instiation
	apb_interface apb_intf (clk_out);

	// DUT instantiation
	apb_slave_top #(.DEPTH(`DEPTH))
	apb_slave_top_inst (
		.PCLK_i  (apb_intf.PCLK_i),    
		.PRESETn_i(apb_intf.PRESETn_i), 
		.PADDR_i (apb_intf.PADDR_i),   
		.PWRITE_i(apb_intf.PWRITE_i), 
		.PWDATA_i(apb_intf.PWDATA_i), 
		.PSTRB_i (apb_intf.PSTRB_i), 
		.PSEL_i  (apb_intf.PSEL_i),
		.PENABLE_i(apb_intf.PENABLE_i),
		.PRDATA_o(apb_intf.PRDATA_o),
		.PREADY_o(apb_intf.PREADY_o),
		.PSLVERR_o(apb_intf.PSLVERR_o)
	);


	// initial block // for test run
	initial begin
		uvm_config_db #(virtual apb_interface)::set (null,"*", "APB_INTF", apb_intf);
		`uvm_info("tb_top", $sformatf("Statring test at system time"), UVM_NONE)
		run_test("base_test");
	end

	// assertion blocks

	// database dump
	initial begin
		//if ($test$plusargs("DUMP")) begin
			`uvm_info ("tb_top", "Dumping VCD file", UVM_NONE)
			$dumpfile("dump.vcd");
			$dumpvars();
		//end
	end

endmodule




