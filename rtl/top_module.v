module top_module(
    input wire clk,
    input wire reset,
    output reg vga_hsync,
    output reg vga_vsync,
    output reg [2:0] vga_red,
    output reg [2:0] vga_green,
    output reg [1:0] vga_blue
);
    
    wire [9:0] x_pos, y_pos;
    wire display_on;
    wire text_pixel, sprite_pixel;
    
    // VGA контроллер
    vga_controller vga(
        .clk(clk),
        .hsync(vga_hsync),
        .vsync(vga_vsync),
        .x_pos(x_pos),
        .y_pos(y_pos),
        .display_on(display_on)
    );
    
    // Текстовый рендерер
    text_renderer text(
        .clk(clk),
        .x(x_pos),
        .y(y_pos),
        .pixel_out(text_pixel)
    );
    
    // Движок спрайтов
    sprite_engine sprite(
        .clk(clk),
        .x_pos(x_pos),
        .y_pos(y_pos),
        .sprite_x(100),  // Фиксированная позиция
        .sprite_y(150),
        .pixel_out(sprite_pixel)
    );
    
    // Смешивание вывода
    always @(posedge clk) begin
        if (display_on) begin
            if (sprite_pixel) begin
                vga_red <= 3'b111;    // Красный спрайт
                vga_green <= 3'b000;
                vga_blue <= 2'b00;
            end else if (text_pixel) begin
                vga_red <= 3'b111;    // Белый текст
                vga_green <= 3'b111;
                vga_blue <= 2'b11;
            end else begin
                vga_red <= 3'b000;    // Черный фон
                vga_green <= 3'b000;
                vga_blue <= 2'b00;
            end
        end else begin
            vga_red <= 3'b000;
            vga_green <= 3'b000;
            vga_blue <= 2'b00;
        end
    end
endmodule