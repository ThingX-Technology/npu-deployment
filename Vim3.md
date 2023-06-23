# NPU setup

1. First, you'll need to download the latest firmware for your VIM3 board from the Khadas website.
2. Once you've downloaded the firmware, extract the files and copy them onto a mi.croSD card using balendaEtcher
3. Insert the microSD card into your VIM3 board and power it on.
4. The VIM3 board should automatically boot from the microSD card and start the firmware update process.
5. Wait for the update process to complete, which may take several minutes.
6. Insert a USB keyboard and mouse into the VIM3 board's USB ports.
7. Connect a monitor to the VIM3 board's HDMI port.
8. Power on the VIM3 board again and wait for it to boot up.

EMMC boot is also possible:
 https://docs.khadas.com/products/sbc/vim3/install-os/start

 ```sh
git clone https://github.com/khadas/ksnn.git
```

2. Install KSNN

```sh
$ pip3 install matplotlib
$ pip3 install ksnn/ksnn-1.3-py3-none-any.whl
```
Run examples provided in the examples folder for NPU usage

## Docs

1. [KSNN Usage](https://docs.khadas.com/products/sbc/vim3/npu/ksnn/ksnn-usage)
3. API Docs: docs/ksnn_user_usage_v1.3.pdf
