# inbaverSys

**inbaverSys** is a Python based Content Centric Networking (CCN) implementation for the 
Internet of Things (IoT). The implementation consist of a single CCN node with a 3-layer 
protocol architecture. It has a modular architecture where each layer can be setup to
use different modules to operate as a functionally specific CCN node. There are 3 types 
of functionally specific nodes that can be configured.

- **Standard Node** - a traditional CCN node such as a client or content server
- **Sensor** - a CCN based sensor node
- **Gateway** - a gateway that connects tradional CCN nodes of the Internet and sensors of a sensor network

The following picture depicting a CCN based network topology shows the different CCN nodes 
that could be configured using the implementation in this repository.

<p align="center">
  <img src="./res/images/net-topology.png" width="600"/>
</p>


## Implementation Architecture

A CCN node consist of a 3-layer protocol architecture. Each layer can be configured with
multiple modules based on the operation expected of the node. The following picture shows 
protocol layers and the possible modules that can be deployed. 

<p align="center">
  <img src="./res/images/protocol-stack.png" width="500"/>
</p>

The description below explains purpose of the layers and the modules tha can be configured.

#### Application Layer

The **Application Layer** is configured on CCN nodes that require the deployment of
applications to request and/or serve content. Examples are client computers that download
content, content servers that host content or IoT gateways that act as the intermediary 
between the Internet and sensor networks.


#### CCN Layer

The **CCN Layer** is where the CCN based forwarder is deployed. There could be different 
flavours of CCN that implements the CCN functionality specific to the node types described
above. For a **Standard Node**, the CCN flavour implements the functionality described in 
the CCN RFCs ([RFC8569](https://datatracker.ietf.org/doc/html/rfc8569) and 
[RFC8609](https://datatracker.ietf.org/doc/html/rfc8609)). An example is any Internet
based node.

For a **Sensor**, a scaled down version of the CCN forwarding is implemented due to the
resource restricted nature of the device. Therefore, it may support a subset of CCN
functionality described in the above RFCs. Additionally, it may have additional
functionality to overcome specficic problems faced in sensor networks (e.g., converting 
long names to short names).

For a **Gateway**, the CCN layer must implement the CCN forwarding that understands the 
CCN of the gateway side and the Internet side - with the ability to translate between 
these 2 flavours.



#### Link Layer

The **Link Layer** is where all the different modules that is able to operate over link
technologies are implemented. Examples are, IP-over-WLAN, IP-over-Ethernet and LoRa.


## Installing and Running

Installing and running the implementation varies based on the type of node on which it is
deployed.

#### Standard Node

A **Standard Node** is a computer that runs an desktop or server operating system (such as 
Linux, MacOS or Windows) and is installed with the Python interpretter. The procedure
of installation and running is as follows.


1. Install Python
2. Copy the `settings.node.py` as `settings.py`
3. Configure the `settings.py` to suit the environment and the operation
4. Run the `main.py` Python script


#### Sensor

A **Sensor** is usually a device with a microcontroller such as the ESP32 that is deployed
with a Python-capable firmware. Refer to the instructions relevant to your microcontroller
on how programs are deployed. Usually, they are run automatically when the device is booted.
The procedure, before the microcontroller specific procedure is applied is as follows.

1. Copy the `settings.sensor.py` as `settings.py`
2. Configure the `settings.py` to suit the environment and the operation
3. Follow the microcontroller specific procedure to deploy on the microcontroller
4. Boot the microcontroller device


#### Gateway

A **Gateway** can be a microprocessor based system such as a Raspberry Pi or a microcontroller 
such as an ESP32 that is able to handle the mixed operation of translating between the CCN 
flavours of standard CCN and CCN operating on sensors. Therefore, the procedure would either
be similar to the **Standard Node** or to the **Sensor**. But, whatever procedure followed,
remember to copy the `settings.gateway.py` as `settings.py`.


## Caveat

This is a work-in-progress. So, not all modules and informational files are implemented. 
The modules developed are located in the [src](./src/) folder.



## Questions or Comments

If you have any questions or comments, please write to us at inbaversys@comnets.uni-bremen.de.

