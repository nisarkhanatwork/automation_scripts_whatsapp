# automation_scripts_whatsapp
To confirm low bandwidth steganography channel in whatsapp
The sender and receiver automation test scripts for Android phones demonstrates the feasibility of this low bandwidth channel:

Frameworks: appium ( test automation framework for Android apps), Selenium.
Python libraries: appium-python-client, selenium 
Other tools/software: adb, nodejs
OS: Windows Host OS ( for Phone1), Ubuntu Guest OS (for Phone 2)

Covert Channel in WhatsApp
--------------------------
"A covert channel is a path that can be used to transfer information in a way not intended by the system's designers. Typically the system has not given authorization for the transmission and has no knowledge of its occurrence."[1]

An example of a covert channel that can be found inside the CPU is that a sender will issue an instruction at some execution port eg., ALU to send a bit 1 and on the reciever side, the latency is measured to execute an instruction on the same port. If the latency is high, it means a 1-bit and 0-bit otherwise. This channel is used to stealthily transfer data between two processes of two different users.

Also in threat modeling, one of the class in which a threat can be classified is repudiation, which occurs when a user denies performing an action and the target of the action has no way to prove otherwise[2].

This weakness can effect the operational security of organizations. And for private users, its potential for illicit use can lead to loss of trust. If proper countermeasures are taken, the misuse of the system can be prevented and the prevention of this makes an application a more Trusted System.

Indeed, covert channels are proliferating as new communication applications and communication infrastructures are built. 

Covert channel in WhatsApp:
WhatsApp has a feature in it which can be used as a covert channel. WhatsApp messenger displays a “typing…” message on the destination user side when the source user starts typing a text. The message in green will be active for a certain period of time after the user stops typing. Even though the user actually wont send the text, we see this message.
So, using this feature of WhatsApp, we can communicate using some encoding with the destined user without actually sending any text, and hopefully (?) without any trace.
Consider two users Alice and Bob who want to communicate secretly using binary encoding, i.e., 1s and 0s. When Alice wants to send a 1 to Bob, he will type a character and waits for some time. Bob will see a message “typing…” for a certain period of time. He stops for a “certain period of time” if he wants to send a 0.

If proper analysis is done to find out the timing of the message displayed and when it goes away, another app or a high bandwidth script can be developed, which as a sender takes a text, encodes it and types characters in WhatsApp to send a message to Bob at proper time and at the receiver end looks at this message “typing…” spread across time. Using these the actual communication can happen by piggybacking on WhatsApp.

The two scripts, Sender: ![./wa_final.py](wa_final.py) and Receiver: ![wa_rec.py](wa_rec.py) are a proof of concept of this covert channel. 
Preview of the video showing the scripts in action is: 

![whatsapp scripts in action](./whatsapp_inaction.gif)

Impact:
   1) If this covert channel is taken care of, WhatsApp can be a more Trustworthy application for private (preventing illicit communication) and commercial communication(not involving in corporate espionage). Because ordinary private and commercial users cannot use/afford tapping mobile network data and its analysis under normal circumstances.
   2) Analysis of this innocuous looking data is cumbersome.
Remember that all the other data that goes through WhatsApp is different than this, as it follows the non-repudiation principle of security.
Action:
If this covert channel is considered risky by Whatsapp, it has the following options after being notified:
   "a) We can eliminate it by modifying the system implementation
    b) We can reduce the bandwidth by introducing noise into the channel
    c) we can monitor it for patterns of usage that indicate someone is trying to exploit it." [3]

One of the perspectives of taking the above options:
   1) Option A:
   Action: Removing the “typing...” message
   Advantage: Removal of the covert channel
   Risk: The augmented reality is lost
   2) Option B: 
   Action: “typing...” message is displayed for a random amount of time, and not for a  constant time period. 
   Advantage: Covert channel bandwidth is decreased, and it can become useless.
   Risk: There will be a slight change in the augmented reality
   3) Option C:
   (WhatsApp is good at blocking users using scripting api’s after it finds them abusing it. But DON’T KNOW whether the messages    related to this covert channel go through WhatsApp servers to analyze patterns...)
   Action: Find patterns in traffic that are using this covert channel, which is cumbersome and block the users.
   Advantage: The “typing...” augmentation of reality remains intact.
   Risk: Cumbersome per user blocking.

References:
1. Common weakness enumeration, CWE-514: Covert Channel, https://cwe.mitre.org/data/definitions/514.html
2. Threat modeling as a basis for security requirements, Suvda Myagmar, Adam J.Lee, William Yurcik
3.CS329E: Spring, 2013: Elements of Security:Covert channels: 
 https://www.cs.utexas.edu/~byoung/cs329e/slides2b-covert-channels-4up.pdf
