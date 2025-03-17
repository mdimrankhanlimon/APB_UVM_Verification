/*
----------------------------------------------------------------------------------------------------------------------------------
 design name : APB Slave 
 designer email : mariam.nijhum@siliconova.com 
 short description : The design operates on the positive edge of the clock signal and an asynchronous active low reset. This design is 			  		     equipped with standard APB slave signals. The data is given through APB signals and can be written in the internal RAM. Later, the data 		     can be read from it.
 last modified date : 04/05/2024
----------------------------------------------------------------------------------------------------------------------------------
*/

`timescale 1ns / 1ps

module apb_slave_top#(
    parameter DATA_WIDTH = 32,
    parameter DEPTH = 1024
)(
    // APB signal interface
    input   wire                      PCLK_i,
    input   wire                      PRESETn_i,
    input   wire [($clog2(DEPTH))-1:0]PADDR_i,
    input   wire                      PWRITE_i,
    input   wire  [DATA_WIDTH-1:0]    PWDATA_i,
    input   wire  [(DATA_WIDTH/8)-1:0]PSTRB_i,
    input   wire                      PSEL_i,
    input   wire                      PENABLE_i,
    output  wire [DATA_WIDTH-1:0]     PRDATA_o,
    output  wire                      PREADY_o,
    output  wire                      PSLVERR_o
 );
 
 // Dual port ram interface
    wire  [DATA_WIDTH - 1:0] dataout_b;
    wire                    write_a;
    wire [($clog2(DEPTH)) - 1:0] addr_a;
    wire [(DATA_WIDTH/8) - 1:0]  byte_sel;
    wire [DATA_WIDTH - 1:0] datain_a;
    wire                    read_b;
    wire [($clog2(DEPTH)) - 1:0] addr_b;   
    
apb_slave #(.DATA_WIDTH(DATA_WIDTH), .DEPTH(DEPTH)) apb_slave_ins1(
	.PCLK_i(PCLK_i), 
	.PRESETn_i(PRESETn_i),
	.PADDR_i(PADDR_i),
	.PWRITE_i(PWRITE_i), 
	.PWDATA_i(PWDATA_i),
	.PSTRB_i(PSTRB_i),
	.PSEL_i(PSEL_i),
	.PENABLE_i(PENABLE_i),
	.PRDATA_o(PRDATA_o),
	.PREADY_o(PREADY_o),
	.PSLVERR_o(PSLVERR_o),
	.dataout_b(dataout_b),
	.write_a(write_a),
	.addr_a(addr_a),
	.byte_sel(byte_sel),
	.datain_a(datain_a), 
	.read_b(read_b),
	.addr_b(addr_b)
);

dual_port_ram #(.DATA_WIDTH(DATA_WIDTH), .DEPTH(DEPTH)) dual_port_ram_ins1 (
	.clk(PCLK_i),
	.resetn(PRESETn_i), 
	.write_a(write_a), 
	.addr_a(addr_a), 
	.byte_sel(byte_sel), 
	.datain_a(datain_a), 
	.read_b(read_b), 
	.addr_b(addr_b), 
	.dataout_b(dataout_b)
);

endmodule
