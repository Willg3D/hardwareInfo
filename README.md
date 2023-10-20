# Hardware Info Inspector Documentation

## Table of Contents

1. [Introduction](#1-introduction)
2. [System Requirements](#2-system-requirements)
3. [Using](#3-using)
4. [User Interface](#4-user-interface)
5. [Using Hardware Info Inspector](#5-using-hardware-info-inspector)
   - [CPU Information](#51-cpu-information)
   - [RAM Information](#52-ram-information)
   - [GPU Information](#53-gpu-information)
   - [Motherboard Information](#54-motherboard-information)
   - [Network Information](#55-network-information)
6. [Troubleshooting](#6-troubleshooting)
7. [Compiling](#7-compiling-hardware-info-inspector)

## 1. Introduction

**Hardware Info Inspector** is a Windows-only application that provides detailed information about your computer's hardware components. With just a few clicks, you can access essential data about your CPU, RAM, GPU, motherboard, and network configuration. This documentation will guide you through the usage of the application.

## 2. System Requirements

To run Hardware Info Inspector, your computer must meet the following system requirements:

- **Operating System**: Windows
- **GPU**: Nvidia Graphics (if not in system, then GPU info section will not work)

## 3. Using

To use Hardware Info Inspector, follow these steps:

1. Download the application from GitHub.

2. Run the executable.

3. Click on User Interface Buttons

## 4. User Interface

The Hardware Info Inspector user interface is straightforward and easy to use. It includes buttons to access information about different hardware components, as follows:

- **CPU Info**: Retrieves information about the Central Processing Unit (CPU).

- **RAM Info**: Displays details about your computer's Random Access Memory (RAM).

- **GPU Info**: Provides information about the Graphics Processing Unit (GPU).

- **Motherboard Info**: Shows details about the motherboard of your computer.

- **Network Info**: Retrieves information about your network configuration.

## 5. Using Hardware Info Inspector

### 5.1. CPU Information

1. Launch the Hardware Info Inspector application.

2. Click the "CPU Info" button in the user interface.

3. The application will display detailed information about your computer's CPU, including current frequency, max frequency, usage per core, total usage and more.

### 5.2. RAM Information

1. Launch the Hardware Info Inspector application.

2. Click the "RAM Info" button in the user interface.

3. The application will display information about your computer's RAM and swap memory, including the total amount of memory, available memory, percentage used.

### 5.3. GPU Information

1. Launch the Hardware Info Inspector application.

2. Click the "GPU Info" button in the user interface.

3. The application will display information about your computer's GPU, including the model, manufacturer, and driver version.

### 5.4. Motherboard Information

1. Launch the Hardware Info Inspector application.

2. Click the "Motherboard Info" button in the user interface.

3. The application will provide information about your computer's motherboard, in the following order manufacturer, product, serial number, and bios version.

### 5.5. Network Information

1. Launch the Hardware Info Inspector application.

2. Click the "Network Info" button in the user interface.

3. The application will retrieve and display information about your network configuration, including network adapters, interface type, SSID, network type, authentication, and encryption type.

## 6. Troubleshooting

If you encounter any issues while using Hardware Info Inspector, first try restarting the application. If not, all information is visible try resizing the windows (no scroll feature is currently implemented). GPU information will only work for Nvidia graphics.

## 7. Compiling Hardware Info Inspector

## Required Python Packages

Hardware Info Inspector relies on the following Python packages:

- **psutil**: Used to get CPU, RAM, virtual space, and network information.
- **gputil**: Used to get Nvidia GPU information.
- **tkinter**: Used to create a basic gui

-**pyinstaller**: Only needed to create an executable

## Compiling
- To compile code all additional python packages from the **Required Python Packages** section must be installed. To create an executable use **pyinstaller**, where gui.py will act as the main, otherwise just run gui.py.
- Code only verified to work on Windows, although it should compile on Windows, MacOS, and Linux.
