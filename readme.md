# Introduction
Do you want to get ski tickets at a vail resort mountian? Are they already sold out for the day that you want to go? If you answered yes to both of the questions, then you are in the right place!

This project will notify you when there are tickets available at the mountain and date that you choose. 

# Resorts
Below are a list of resorts that this program will work at. When entering the mountain into the command line, please use the right hand column. This may be changed in a future update, but no promises. 

| Name                          | Command Line          |
| ----------------------------- | --------------------- |
| Vail                          | vail                  |
| Beaver Creek                  | beavercreek           |
| Breckenridge                  | breckenridge          |
| Crested Butte                 | skicb                 |
| Keystone                      | keystoneresort        |
| Park City                     | parkcitymountain      |
| Heavenly                      | skiheavenly           |
| Northstar                     | northstarcalifornia   |
| Kirkwood                      | kirkwood              |
| Steven's Pass                 | stevenspass           |
| Mount Sunapee                 | mountsunapee          |
| Okemo                         | okemo                 |
| Stowe                         | stowe                 |
| Hunter Mountain               | huntermtn             |
| Mount Snow                    | mountsnow             | 
| Attitash                      | attitash              |
| Wildcat                       | skiwildcat            |
| Crotched                      | crotchedmtn           |
| Liberty                       | libertymountainresort |
| Roundtop                      | skiroundtop           |
| Whitetail                     | skiwhitetail          |
| Jack Frost Big Boulder        | jfbb                  |
| Afton Alps                    | aftonalps             |
| Mt Brighton                   | mtbrighton            |
| Wilmot                        | wilmotmountain        |
| Alpine Valley                 | alpinevalleyresort    |
| Boston Mills & Brandywine     | bmbw                  |
| Mad River Mountain            | skimadriver           |
| Snow Creek                    | skisnowcreek          |
| Paoli Peaks                   | paolipeaks            |
| Whistler Blackcomb            | whistlerblackcomb     |

# Requirements
- Python >= 3.8
- argparse
- requests-html

# Installation
Git pull the package and then use pip to install the requirements. Then see the following section for how to run the script.

# Usage
Run `lift_tickets.py` as you would any python script. Here is an example, including a phone number and an email.

`python3 lift_tickets.py libertymountainresort 02/21/2021 -p 5555555555 -c att -e fake@gmail.com`

The output of help is shown below.

```
usage: lift_tickets.py [options] mountain date

Getting you sold out lift tickets.

positional arguments:
  mountain              The mountain you want to ski at. List avaliabe here _____.
  date                  Date in the format MM/DD/YYYY.

optional arguments:
  -h, --help            show this help message and exit
  -e email, --email email
                        Emails the given email when tickets are avaliable.
  -p phone, --phone phone
                        Texts the given phone when tickets are avaliable. Enter #########, no dashes.
  -c carrier, --carrier carrier
                        Specifies the carrier of the phone. Necessary when using phone option. Options
                        are att, tmobile, verizon, or sprint.
  -t timeout, --timeout timeout
                        Timeout for email and text in seconds. Defult is 2 minutes (120 seconds).
  -q, --quiet           Decreses the amount of output.
```

# Issues
If you run into any issues please do not hesitate to open an issue on github and I will be happy to help :).

# Maintainers
- Dalton Herrold

# Note
This was a fun weekend project to make and got me skiing quite a few times that I otherwise wouldn't have been able to. Have fun shredding the slopes! :) 