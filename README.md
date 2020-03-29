# record-harddrive-led

The led lights continuously when memory capacity is low and blinks when memory capacity is extremely low. 

# Autostart python script:

* `sudo nano /lib/systemd/system/blink.service`

Enter the following text into the document:

    [Unit]
    Description=Blink my LED
    After=multi-user.target

    [Service]
    Type=simple
    ExecStart=/home/ubuntu/Desktop/YourPythonScript.py
    Environment=DISPLAY=:0
    Environment=XAUTHORITY=/home/ubuntu/.Xauthority
    Restart=always
    RestartSec=5s
    KillMode=process
    TimeoutSec=infinity
    
    [Install]
    WantedBy=graphical.target


* Save and Exit.

* Tell systemd to recognize your service:

`sudo systemctl daemon-reload`

`sudo systemctl enable blink.service`


