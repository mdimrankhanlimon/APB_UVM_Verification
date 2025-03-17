/*
---------------------------------------------------
 design name : APB Slave and dual port ram interface
 designer email : mariam.nijhum@siliconova.com 
 short description : The design operates on the positive edge of the clock signal and an asynchronous active low reset. One aspect of this design is
 equipped with standard APB slave signals, while the other aspect features dual-port RAM signals for seamless communication with
 internal RAM.
 last modified date : 04/05/2024
----------------------------------------------------
*/

 
module apb_slave
#(
    parameter DATA_WIDTH = 32,
    parameter DEPTH = 1024

)(
    
    // APB signal interface
    input   wire                       PCLK_i,
    input   wire                       PRESETn_i,
    input   wire [($clog2(DEPTH))-1:0] PADDR_i,
    input   wire                       PWRITE_i,
    input   wire [DATA_WIDTH-1:0]      PWDATA_i,
    input   wire [(DATA_WIDTH/8)-1:0]  PSTRB_i,
    input   wire                       PSEL_i,
    input   wire                       PENABLE_i,
    output  reg  [DATA_WIDTH-1:0]      PRDATA_o,
    output  reg                        PREADY_o,
    output  reg                        PSLVERR_o,
 
 // Dual port ram interface
    input  wire [DATA_WIDTH - 1:0]      dataout_b,
    output wire                         write_a,
    output wire [($clog2(DEPTH)) - 1:0] addr_a,
    output wire [(DATA_WIDTH/8) - 1:0]  byte_sel,
    output wire [DATA_WIDTH - 1:0]      datain_a,
    output wire                         read_b,
    output wire [($clog2(DEPTH)) - 1:0] addr_b   
  );
 
 // for detecting sel to enable delay
    reg [1:0] count;
    reg       flop;
    reg       flop2;
    wire      temp_err;

	always@(posedge PCLK_i)begin
		count = (PSEL_i & !PENABLE_i & PREADY_o) ? (count + 1):'b0;
	end

	always@(posedge PCLK_i)begin
		flop  <= temp_err;
		flop2 <= flop;
	end

    assign temp_err = (count >= 2'd2);
    assign addr_a   = PADDR_i;
    assign addr_b   = PADDR_i;
    assign write_a  = PWRITE_i & PSEL_i & PENABLE_i & PREADY_o;
    assign write_a  = PWRITE_i & PSEL_i & PENABLE_i & PREADY_o;
    assign read_b   = (!PWRITE_i) & PENABLE_i & PREADY_o;
    assign datain_a = PWDATA_i;
    assign byte_sel = PWRITE_i ? PSTRB_i : 'd0; 
    
    reg [1:0] nextstate;
    reg [1:0] prstate;
    
    parameter [1:0] IDLE   = 2'b00;
    parameter [1:0]	SETUP  = 2'b01;
    parameter [1:0] ACCESS = 2'b10;
    
    always@(posedge PCLK_i or negedge PRESETn_i)begin
        if(!PRESETn_i)begin
            prstate <= IDLE;     
        end
        else begin
            prstate <= nextstate;    
        end
    end
    
    always@(*)begin
        case(prstate)
            IDLE:
            begin
                PRDATA_o  = 'd0;
                PSLVERR_o = 'd0;
                PREADY_o  = 1'b0;
                nextstate = PSEL_i ? SETUP : IDLE; 
            end
            
            SETUP:
            begin
                PREADY_o  = 1'b0;
                PRDATA_o  = 'd0;
                PSLVERR_o = 1'b0;
                nextstate = PENABLE_i ? ACCESS : SETUP;
            end
    
            ACCESS:
            begin
                PREADY_o  = 1'b1;
                PRDATA_o  = dataout_b;
                PSLVERR_o = ((!PWRITE_i)&(|PSTRB_i)) | flop2;
    			count     = 2'd0;
                nextstate = PSEL_i ? SETUP : IDLE;
            end
    		
        endcase
    end
endmodule

