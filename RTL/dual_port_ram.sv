/*
---------------------------------------------------
 design name : Dual port ram
 designer email : mariam.nijhum@siliconova.com 
 short description + limitation
 
 last modified date : 27/04/2024
 modified by : rashidshabab58@gmail.com
----------------------------------------------------
*/


 
//module dual_port_ram#(
//    parameter DATA_WIDTH = 32,
//    parameter DEPTH = 1024,
//  	parameter ADDR_WIDTH = $clog2(DEPTH),
//    parameter BYTE_LANE = DATA_WIDTH/8
//)(
//    input       clk,
//    input       resetn,
//
//    // port a signals  
//    input                          write_a,  // only for write data
//    input       [ADDR_WIDTH - 1:0] addr_a,
//    input       [BYTE_LANE-1:0] byte_sel,
//    input       [DATA_WIDTH - 1:0] datain_a,
//    
//    // port b signals
//    input                          read_b,  // only for read data
//    input       [ADDR_WIDTH - 1:0] addr_b,
//    output      [DATA_WIDTH - 1:0] dataout_b
//);
//
//  reg [DATA_WIDTH-1:0]mem[DEPTH - 1:0]; 
//  reg [DATA_WIDTH - 1:0]outData;
//
//always@(posedge clk)begin
//	mem[(addr_a) + 0] <= (write_a & byte_sel[0]) ? datain_a[((8)*0) + 7 : (8)*0] : mem[(addr_a) + 0];
//    mem[(addr_a) + 1] <= (write_a & byte_sel[1]) ? datain_a[((8)*1) + 7 : (8)*1] : mem[(addr_a) + 1];
//    mem[(addr_a) + 2] <= (write_a & byte_sel[2]) ? datain_a[((8)*2) + 7 : (8)*2] : mem[(addr_a) + 2];
//    mem[(addr_a) + 3] <= (write_a & byte_sel[3]) ? datain_a[((8)*3) + 7 : (8)*3] : mem[(addr_a) + 3];
//
//	
//	if(!resetn)begin
//		outData <= 'b0;
//	end else begin
//		outData <= {mem[(addr_b) + 3], mem[(addr_b) + 2], mem[(addr_b) + 1], mem[(addr_b) + 0]}; 
//	end
//
//
//end
//  
//   assign dataout_b = (resetn & read_b & !write_a ) ? outData : 'h0;
//  
////   assign dataout_b = outData;
//  
////   assign dataout_b = (read_b) ? {mem[(addr_b) + 3], mem[(addr_b) + 2], mem[(addr_b) + 1], mem[(addr_b) + 0]} : 0;
//  
////  assign dataout_b = (read_b) ? {mem[(addr_b) + 3], mem[(addr_b) + 2], mem[(addr_b) + 1], mem[(addr_b) + 0]} : 'hz;
//  
//endmodule

/*
---------------------------------------------------
 design name : Dual port ram
 designer email : mariam.nijhum@siliconova.com 
 short description + limitation
 
 last modified date : 27/04/2024
 modified by : rashidshabab58@gmail.com
----------------------------------------------------
*/


 

module dual_port_ram #(
    parameter DATA_WIDTH = 32,
    parameter DEPTH = 1024,
    parameter ADDR_WIDTH = $clog2(DEPTH),
    parameter BYTE_LANE = DATA_WIDTH / 8
)(
    input       clk,
    input       resetn,
    
    // Port A signals
    input                     write_a,
    input  [ADDR_WIDTH - 1:0] addr_a,
    input  [BYTE_LANE - 1:0]  byte_sel,
    input  [DATA_WIDTH - 1:0] datain_a,
    
    // Port B signals
    input       read_b,
    input  [ADDR_WIDTH - 1:0] addr_b,
    output [DATA_WIDTH - 1:0] dataout_b
);

    reg [DATA_WIDTH-1:0] mem [0:DEPTH-1];
    reg [DATA_WIDTH-1:0] outData;

    always @(posedge clk) begin
        if (!resetn) begin
            outData <= 'b0;
        end else begin
            // Read data from memory and concatenate bytes
            outData <= {mem[addr_b][31:24], mem[addr_b][23:16], mem[addr_b][15:8], mem[addr_b][7:0]};
        end
        
        // Write operation to memory
        if (write_a) begin
            // Selectively update memory based on byte_sel
            if (byte_sel[0]) mem[addr_a][7:0]   <= datain_a[7:0];
            if (byte_sel[1]) mem[addr_a][15:8]  <= datain_a[15:8];
            if (byte_sel[2]) mem[addr_a][23:16] <= datain_a[23:16];
            if (byte_sel[3]) mem[addr_a][31:24] <= datain_a[31:24];
        end
    end

    // Output data based on read operation
    assign dataout_b = (resetn & read_b & !write_a) ? outData : 'h0;

endmodule
