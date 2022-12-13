# Auto DNS record updater

This simple python script automates the process of updating your AAAA records with an IPv6 address assigned dynamically on boot.

## Instructions

### 1. Create `.env` file.

Create a copy of `.env.example` and name it as `.env`. Update the details accordingly.
You can find your Zone ID on the overview page of your CloudFlare dashboard.

### 2. Fetch your Record ID

Create a record dump by running
```
python dump.py
```

This will create a file called `record-dump.json` containing all your Zone Records. Copy the `id` of your preferred record and paste it in the `.env` file.

### 3. Setup to run on boot

Copy the contents of `ipupdate.service.example` into a new file

```
sudo nano /etc/systemd/system/ipupdate.service
```
(You can name the file anything you want)

Update the `ExecStart` path to match your setup.


### 4. Enable the service

```
sudo systemctl enable ipupdate.service
```

This will enable the service to run on boot.
You can also start the service manually by running
```
sudo systemctl start ipupdate.service
```

To disable the service, run
```
sudo systemctl disable ipupdate.service
```

Thats it! You should now be able to see your IPv6 address on your CloudFlare dashboard on boot.
