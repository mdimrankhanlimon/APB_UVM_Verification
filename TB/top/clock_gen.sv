
module clock_gen (output reg clk);
  
	parameter FREQ    = 100;       // in MHZ
	parameter PHASE   = 0; 		 // in degrees
	parameter DUTY    = 50;  	     // in percentage 
	parameter JITTER  = 0;  	     // in percentage 
	
	real clk_pd  		= 1.0/(FREQ * 1e6) * 1e9; 	// convert to ns
	real clk_on  		= DUTY/100.0 * clk_pd;
	real clk_off 		= (100.0 - DUTY)/100.0 * clk_pd;
	real quarter 		= clk_pd/4;
	real start_dly    = quarter * PHASE/90;
	int jitter        = JITTER/2;
	
	
	// Initialize variables to zero
	initial begin
		clk <= 0;
	end
	
										    
	initial begin
		#(start_dly);
		forever begin
			#(clk_off+$random %(jitter)) clk = 1;
			#(clk_on+$random %(jitter))  clk = 0;
		end
	end


endmodule





