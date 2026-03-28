# Retro Game Console Project

A demonstration retro game console implemented in Verilog with VGA graphics output.

## 🎮 Features

- **VGA controller** 640x480
- **Text output** "Hello Retro!"
- **Pixel sprites** 16x16
- **Vector graphics** (3D cube)
- **Graphics rotation**
- **Interactive control**

## 📁 Project Structure
├── rtl/ # Verilog source files
├── sim/ # Test environments and simulation
├── fonts/ # Pixel fonts
├── sprites/ # Sprite data
├── python/ # Helper scripts
├── screenshots/ # Screenshots of the project
└── README.md # This file

## 🚀 Quick Start

```bash
# Run simulation
cd sim
iverilog -o simulation tb_demo.v ../rtl/*.v
vvp simulation

