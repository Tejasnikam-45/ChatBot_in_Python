from flask import Flask, request, jsonify
app = Flask(__name__)

qa_pairs = {
    "Hii":"Hello Tejas!, How can i help you.?",
    "What is C?": "C refers to the C programming language, which is a widely used, efficient, and versatile programming language developed in the early 1970s. It is known for its simplicity, power, and direct access to hardware, making it suitable for system software, application development, and embedded systems.",
    "What is Python?":"Python is a high-level, interpreted programming language known for its simplicity and readability. It emphasizes code readability and has a clear, concise syntax, making it popular among beginners and experienced programmers alike. Python supports multiple programming paradigms and is widely used in web development, data analysis, artificial intelligence, scientific computing, and more.",
    "What is Frontend.": "the front end refers to the user interface and presentation layer of a software application or website. It includes everything that users interact with directly, such as web pages, graphical elements, buttons, forms, and menus. Front-end development involves creating these components using technologies like HTML, CSS, and JavaScript to ensure a seamless and engaging user experience.",
    "Explain DSA in detail.":"DSA stands for Data Structures and Algorithms.It's a fundamental concept in computer science and software engineering, crucial for designing efficient and scalable solutions to various computational problems. Let's break down DSA in detail:Data Structures:Data structures are ways of organizing and storing data so that it can be accessed and modified efficiently. They provide different ways of representing data, each optimized for specific operations.Here are some common data structures:Arrays: A collection of elements stored at contiguous memory locations, allowing random access using indices.Linked Lists: A collection of nodes, where each node contains data and a reference (pointer) to the next node in the sequence.Stacks: A Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end.Queues: A First-In-First-Out (FIFO) data structure where elements are added at the rear and removed from the front.Trees: Hierarchical data structures consisting of nodes connected by edges, typically with one designated as the root node.Graphs: Non-linear data structures consisting of nodes (vertices) connected by edges, allowing for complex relationships.",
    "What is COA?":"Computer architecture is the design and organization of computer systems, including their components and how they interact with each other. This field encompasses both the hardware components of a computer system, such as the central processing unit (CPU), memory, input/output devices, and the system's organization, including the instruction set architecture (ISA) and the overall system architecture.",
    "What is AT?":"Automata theory is a branch of theoretical computer science that deals with the study of abstract machines and computational models, known as automata, and the languages they can recognize or generate.",
    "What is OS?":"OS commonly stands for Operating System. An operating system is a software that acts as an intermediary between computer hardware and the applications running on it. It manages the computer's resources, including the processor, memory, storage devices, input/output devices, and network connections, and provides a user interface for interacting with the system.",
    "What is DSA?":"Data Structures and Algorithms are fundamental concepts in computer science and are widely used in software development, programming, and algorithmic problem-solving. Understanding DSA is crucial for designing efficient algorithms, writing high-performance code, and solving complex computational problems.",
    "What are the primary technologies used in frontend development?":"HTML (Hypertext Markup Language), CSS (Cascading Style Sheets), and JavaScript are the core technologies used in frontend development. HTML provides the structure, CSS styles the elements, and JavaScript adds interactivity.",
    "What is responsive web design?":"Responsive web design is an approach to designing and coding websites so that they provide an optimal viewing experience across a wide range of devices and screen sizes, from desktop computers to mobile phones.",
    "What are some popular CSS preprocessors?":"Sass (Syntactically Awesome Stylesheets) and Less are two popular CSS preprocessors. They extend the capabilities of CSS by introducing features like variables, nesting, and mixins.",
    "What is a CSS framework?":"A CSS framework is a pre-prepared library that contains standardized, reusable code for common web design tasks. Frameworks like Bootstrap and Foundation provide a grid system, pre-styled UI components, and responsive design features.",
    "What is AJAX?":"AJAX (Asynchronous JavaScript and XML) is a technique for creating dynamic web pages by exchanging small amounts of data with the server behind the scenes. This allows web pages to be updated asynchronously without reloading the entire page.",
    "What are some tools for debugging and optimizing frontend code?":"Browser developer tools like Chrome DevTools and Firefox Developer Tools provide features for inspecting HTML, CSS, and JavaScript, debugging code, profiling performance, and optimizing web applications. Other tools like Lighthouse and WebPageTest help analyze and improve website performance and accessibility.",
    "What programming languages are commonly used in backend development?":"Popular programming languages for backend development include JavaScript (Node.js), Python (Django, Flask), Java (Spring Boot), Ruby (Ruby on Rails), and PHP (Laravel).",
    "What is RESTful API?":" RESTful API (Representational State Transfer) is an architectural style for designing networked applications. It uses standard HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources, typically using JSON or XML for data exchange.",
    "What is the difference between SQL and NoSQL databases?":"SQL databases, such as MySQL and PostgreSQL, are relational databases that store data in tables with predefined schemas and support SQL queries. NoSQL databases, like MongoDB and Cassandra, are non-relational databases that store data in flexible, schema-less formats and use various query languages or APIs.",
    "What is the role of ORM in backend development?":"ORM (Object-Relational Mapping) is a technique used to convert data between incompatible systems (such as object-oriented programming languages and relational databases). It allows developers to work with relational databases using object-oriented paradigms, simplifying database interaction and reducing repetitive code.",
    "What is a microservices architecture?":"A microservices architecture is an architectural style that structures an application as a collection of loosely coupled, independently deployable services. Each service is organized around a specific business function and communicates with other services through well-defined APIs.",
    "What is caching, and why is it important in backend development?":"Caching involves storing frequently accessed data in temporary storage to improve performance and reduce the load on backend servers. It helps minimize response times and bandwidth usage by serving cached data instead of re-computing or fetching it from the original source",
    "What are some tools for backend development, deployment, and monitoring?":"Tools commonly used in backend development include IDEs (Integrated Development Environments) like Visual Studio Code and JetBrains IntelliJ IDEA, version control systems like Git, continuous integration and deployment (CI/CD) tools like Jenkins and Travis CI, and monitoring tools like Prometheus and Grafana for tracking application performance and health.",
    "What is session management in backend development?":"Session management involves keeping track of user sessions on a web application. It typically includes generating and storing unique session identifiers, managing session data, and handling session expiration and invalidation.",
    "What are the main functions of an Operating System?":"The main functions of an Operating System include managing hardware resources (CPU, memory, storage devices), providing a user interface, facilitating communication between hardware and software, managing files and directories, and handling system security and error handling.",
    "What are the different types of Operating Systems?":"Operating Systems can be categorized into various types, including: Single-user/single-tasking OS (e.g., MS-DOS) Single-user/multi-tasking OS (e.g., Windows, macOS)Multi-user/multi-tasking OS (e.g., Linux, Unix)Real-time OS (RTOS) for time-sensitive applications (e.g., industrial automation)",
    "What is virtual memory?":"Virtual memory is a memory management technique used by Operating Systems to simulate additional main memory (RAM) beyond the physical memory installed in a computer. It allows programs to use more memory than is physically available by temporarily transferring data to disk storage.",
    "What is a file system?":"A file system is a method for storing and organizing computer files and the data they contain. It defines how files are named, stored, and organized on storage devices such as hard drives, SSDs, and flash drives.",
    "What is multitasking/multiprocessing in an Operating System?":"Multitasking (in single-core CPUs) or multiprocessing (in multi-core CPUs) refers to the ability of an Operating System to run multiple processes or tasks concurrently. It shares CPU time among multiple tasks to give the appearance of simultaneous execution.",
    "What is process scheduling?":"Process scheduling is the method used by Operating Systems to manage the execution of processes (or tasks) in a system with multiple competing processes. It determines which process gets access to the CPU and for how long, based on scheduling algorithms like Round Robin, First-Come-First-Served, or Shortest Job Next.",
    "What is a device driver?":"A device driver is a software component that allows the Operating System to communicate with hardware devices like printers, graphics cards, and storage devices. It provides a standardized interface for interacting with hardware, abstracting the complexity of device-specific operations.",
    "What is kernel in an Operating System?":"The kernel is the core component of an Operating System that manages system resources, provides essential services, and acts as an intermediary between software applications and hardware devices.",
    "What is the difference between a 32-bit and 64-bit Operating System?":"The main difference between 32-bit and 64-bit Operating Systems lies in the size of memory addresses they can access. A 32-bit OS can address up to 4 gigabytes of memory, while a 64-bit OS can address much larger amounts of memory, theoretically up to 16 exabytes. Additionally, 64-bit systems can execute 64-bit software, which can offer performance advantages and access to more advanced features.",
    "What are the different types of computer networks?":"Computer networks can be classified into various types based on their size, geographic scope, and functionality. Common types include LANs (Local Area Networks), WANs (Wide Area Networks), MANs (Metropolitan Area Networks), WLANs (Wireless Local Area Networks), and the Internet.",
    "What is network topology?":"Network topology refers to the physical or logical layout of a computer network, including the arrangement of nodes and connecting links. Common network topologies include bus, star, ring, mesh, and hybrid topologies.",
    "What is the OSI model, and why is it important in networking?":"The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a communication system into seven layers. It helps in understanding and designing network architectures by providing a hierarchical structure for network protocols and communication.",
    "What is IP addressing?":"IP addressing is a method used to uniquely identify devices on a network. It involves assigning IP addresses, which are numerical labels, to network interfaces, enabling devices to communicate with each other within an IP-based network.",
    "What is subnetting?":"Subnetting is the process of dividing a larger network into smaller, more manageable sub-networks, or subnets. It helps in optimizing network performance, improving security, and efficiently allocating IP addresses",
    "What is a router, and what role does it play in networking?":"A router is a networking device that forwards data packets between computer networks. It operates at the network layer (Layer 3) of the OSI model and uses routing tables to determine the best path for packet delivery.",
    "What is the purpose of network security?":"Network security aims to protect network resources and data from unauthorized access, misuse, modification, or disruption. It involves implementing various security measures, such as firewalls, encryption, access controls, and intrusion detection systems.",
    "What is Quality of Service (QoS) in networking?":"Quality of Service (QoS) refers to the capability of a network to provide different levels of service to different types of traffic, based on factors such as bandwidth, latency, packet loss, and jitter. QoS mechanisms prioritize certain types of traffic to ensure better performance for critical applications.",
    "What are the key considerations in network design?":"Key considerations in network design include scalability, reliability, performance, security, ease of management, and cost-effectiveness. A well-designed network architecture should meet the current and future needs of the organization while minimizing potential risks and maximizing efficiency.",
    "What are some popular CNN architectures?":"Popular CNN architectures include LeNet, AlexNet, VGG, GoogLeNet (Inception), ResNet, and MobileNet. These architectures vary in depth, complexity, and performance on different tasks.",
    "What are some common applications of CNNs?":"CNNs are used in various computer vision tasks, including image classification, object detection, facial recognition, image segmentation, and image generation.",
    "What is Computer Organization and Architecture (COA)?":"COA is a field of computer science that deals with the internal structure and operation of computer systems. It encompasses topics such as instruction set architecture, processor design, memory systems, input/output systems, and system organization.",
    "What is the difference between Computer Organization and Computer Architecture?":"Computer organization refers to the way hardware components are arranged and interact to form a computer system, while computer architecture refers to the design attributes of the system visible to the programmer, such as instruction sets and addressing modes.",
    "What is the role of the CPU in a computer system?":"The CPU (Central Processing Unit) is the primary component responsible for executing instructions and performing calculations in a computer system. It fetches instructions from memory, decodes them, executes them, and then stores the results",
    "What is the Von Neumann architecture?":"The Von Neumann architecture, proposed by John von Neumann in the 1940s, is a computer architecture design that stores program instructions and data in the same memory space. It consists of a CPU, memory, input/output devices, and a bus system for communication.",
    "What are the main components of a CPU?":"The main components of a CPU include the arithmetic logic unit (ALU), control unit (CU), registers, and the CPU cache. The ALU performs arithmetic and logical operations, the CU coordinates the execution of instructions, registers temporarily hold data and instructions, and the cache stores frequently accessed data for faster retrieval.",
    "What is the difference between RISC and CISC architectures?":"RISC (Reduced Instruction Set Computer) architectures have a small and simple set of instructions, with each instruction executing in a single clock cycle. CISC (Complex Instruction Set Computer) architectures have a larger and more complex instruction set, with some instructions taking multiple clock cycles to execute.",
    "What is the memory hierarchy?":"The memory hierarchy refers to the arrangement of different types of memory in a computer system, ranging from fast and expensive memory (e.g., CPU registers and cache) to slower and cheaper memory (e.g., main memory and secondary storage). This hierarchy is designed to optimize performance and cost.",
    "What is pipelining in CPU design?":"Pipelining is a technique used in CPU design to improve instruction throughput by overlapping the execution of multiple instructions. It divides the instruction execution process into stages, with each stage performing a different part of the instruction execution process.",
    "What is the role of an operating system in COA?":"The operating system manages the resources of a computer system, including the CPU, memory, storage devices, and input/output devices. It provides a layer of abstraction between the hardware and software, allowing applications to run efficiently and facilitating user interaction with the system.",
    "What are some recent trends in COA?":"Recent trends in COA include the rise of multicore processors, which contain multiple CPU cores on a single chip, as well as the increasing use of parallel computing architectures and the integration of specialized hardware accelerators for tasks such as machine learning and graphics processing. Additionally, energy-efficient design techniques and advances in memory technologies are important areas of research and development in COA."
    }

def get_response(user_input):
    user_input = user_input.lower()
    
    for question, answer in qa_pairs.items():
        if user_input in question.lower():
            return answer
    
    return "Sorry, I don't understand that."

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json["msg"]
    response = get_response(user_input)
    return jsonify(response)

@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)