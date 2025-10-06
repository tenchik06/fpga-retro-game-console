`timescale 1ns/1ps

module tb_simple;
    reg clk;
    
    initial begin
        clk = 0;
        $display("Starting simulation...");
        
        // Создаем VCD файл
        $dumpfile("sim/test_wave.vcd");
        $dumpvars(0, tb_simple);
        
        // Простая симуляция
        #100 $display("Simulation completed");
        $finish;
    end
    
    always #10 clk = ~clk;
endmodule