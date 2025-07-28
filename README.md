
<a name="readme-top"></a>

# <div align="center"> Streaming Hub</div>

<img width="1346" height="465" alt="stream" src="https://github.com/user-attachments/assets/3cc744e6-2387-4701-a8a5-680963d4e483" />


# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
    - [Live Demo](#live-demo)
    - [Walkthrough](#Walkthrough)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)



## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

  <ul>
  <li><a href="https://microverse.notion.site/HTML-CSS-Get-a-head-start-275eb85fd34b4416aa06ec635d69cdaf">Python</li>
  <li><a href="https://microverse.notion.site/HTML-CSS-Get-a-head-start-275eb85fd34b4416aa06ec635d69cdaf">Kafka</a></li>
      <li><a href="https://microverse.notion.site/HTML-CSS-Get-a-head-start-275eb85fd34b4416aa06ec635d69cdaf">PostgreSQL</a></li>
      <li><a href="https://microverse.notion.site/HTML-CSS-Get-a-head-start-275eb85fd34b4416aa06ec635d69cdaf">JAVA</a></li>    
      <li><a href="https://react.dev/learn/start-a-new-react-project#create-react-app">Grafana</a></li>

</ul>

###  Key Features <a name="key-features"></a>

-  Integration with external APIs: Intergrate Kafka Sourcing Data from an API
-  Harness the data in a warehouase, perform transformations
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🌐 Live Demo <a name="#live-demo"></a>

<img width="1366" height="726" alt="Kafka setup" src="https://github.com/user-attachments/assets/0db8799b-4cb7-4dd3-b15e-1906aabe419b" />

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 👁 Walkthrough <a name="#Walkthrough"></a>


## 💻 Getting Started with Kafka <a name="getting-started"></a>

To run Kafka:

Notes to start your Kafka after installation in your local machine:


To start Zookepeer - .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

To start Kafka server - .\bin\windows\kafka-server-start.bat .\config\server.properties

To create Topic (In this case topic name is Stream) - kafka-topics.bat --create --bootstrap-server localhost:9092 --topic Stream

To create a producer to receive requests from the API - Kafka\bin\windows>kafka-console-producer.bat --broker-list localhost:9092 --topic Stream

To create a consumer to display received requests - kafka-console-consumer.bat --topic Stream --bootstrap-server localhost:9092 --from-beginning

### Setup

Clone this repository to your desired folder:

> cd my-folder
> git clone https://github.com/Jonathan-Rop/Project-Two-Streaming-Project-

### Prerequisites

To run this project you need:

- GitHub account;
- git installed on your OS.
- Python
- Kafka Byte
- Kafka
- PostgrSQL


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 👤 Jonathan Kiprono

