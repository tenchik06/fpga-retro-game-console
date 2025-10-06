`timescale 1ns/1ps

module tb_demo_fixed;
    reg clk;
    reg [1:0] rotation = 0;
    wire [9:0] x_pos, y_pos;
    wire display_on;
    wire text_pixel, sprite_pixel, vector_pixel;
    
    // VGA контроллер
    vga_controller vga(
        .clk(clk),
        .hsync(),
        .vsync(), 
        .x_pos(x_pos),
        .y_pos(y_pos),
        .display_on(display_on)
    );
    
    // Текстовый рендерер (Hello)
    text_renderer text(
        .clk(clk),
        .x(x_pos),
        .y(y_pos),
        .pixel_out(text_pixel)
    );
    
    // Спрайтовый движок
    sprite_engine sprite(
        .clk(clk),
        .x_pos(x_pos),
        .y_pos(y_pos),
        .sprite_x(100),
        .sprite_y(150),
        .pixel_out(sprite_pixel)
    );
    
    // Векторный рендерер (куб)
    vector_renderer vector(
        .clk(clk),
        .x_pos(x_pos),
        .y_pos(y_pos),
        .rotation(rotation),
        .pixel_out(vector_pixel)
    );
    
    initial begin
        clk = 0;
        forever #10 clk = ~clk; // 50MHz
    end
    
    initial begin
        $dumpfile("sim/demo_wave.vcd");
        $dumpvars(0, tb_demo_fixed);
        
        $display("Starting Demo Simulation...");
        
        // Тестируем вращение
        #100000;
        rotation = 1;
        #100000;
        rotation = 2; 
        #100000;
        rotation = 3;
        #100000;
        
        $display("Demo simulation completed!");
        $finish;
    end
endmodule