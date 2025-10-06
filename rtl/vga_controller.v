module vga_controller(
    input wire clk,
    output reg hsync,
    output reg vsync,
    output reg [9:0] x_pos,
    output reg [9:0] y_pos,
    output reg display_on
);
    // Параметры VGA 640x480
    parameter H_DISPLAY = 640;
    parameter H_FRONT = 16;
    parameter H_SYNC = 96;
    parameter H_BACK = 48;
    parameter H_TOTAL = 800;
    
    parameter V_DISPLAY = 480;
    parameter V_FRONT = 10;
    parameter V_SYNC = 2;
    parameter V_BACK = 33;
    parameter V_TOTAL = 525;
    
    reg [9:0] h_count = 0;
    reg [9:0] v_count = 0;
    
    always @(posedge clk) begin
        if (h_count < H_TOTAL - 1)
            h_count <= h_count + 1;
        else begin
            h_count <= 0;
            if (v_count < V_TOTAL - 1)
                v_count <= v_count + 1;
            else
                v_count <= 0;
        end
    end
    
    always @* begin
        hsync = ~((h_count >= (H_DISPLAY + H_FRONT)) && 
                 (h_count < (H_DISPLAY + H_FRONT + H_SYNC)));
        vsync = ~((v_count >= (V_DISPLAY + V_FRONT)) && 
                 (v_count < (V_DISPLAY + V_FRONT + V_SYNC)));
        display_on = (h_count < H_DISPLAY) && (v_count < V_DISPLAY);
        x_pos = (h_count < H_DISPLAY) ? h_count : 0;
        y_pos = (v_count < V_DISPLAY) ? v_count : 0;
    end
endmodule