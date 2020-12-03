<br />
<p align="center">
   <h3 align="center">README</h3>
   <br />
   <p align="center">Tech interview leboncoin</p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#materials">Materials</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#tests">Tests</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project
Find the biggest square in a map

### Materials
- Subject(hhttps://github.com/Sylvaindce/tech_interview_leboncoin/tree/main/materials/Subject_Exercice_Python_Algo_leboncoin.pdf)
- Map Generator(https://github.com/Sylvaindce/tech_interview_leboncoin/tree/main/materials/map_gen.py)

### Built With
* [Python3](https://www.python.org/)

## Getting Started
Pytest is not mandatory if you don't want to launch the unit test.

### Prerequisites
* Python3
* Pytest
  ```sh
  pip3 install -r requirements.txt
  ```

### Installation
```sh
  make re
```

## Usage
How to launch the program

  ```sh
  ./find_square map_file.txt map_file_2.txt ...
  ```
or
  ```sh
  python3 src/map_solver/find_square.py map_file.txt map_file_2.txt ...
  ```

It can run in standalone mode if you start the program without any arguments
  ```sh
  make run
  ```

## Tests
To launch the unit test
  ```sh
  make test
  ```

## Contact

DECOMBE Sylvain - sylvain.decombe@epitech.eu

Project Link: [https://github.com/Sylvaindce/tech_interview_leboncoin](https://github.com/Sylvaindce/tech_interview_leboncoin)