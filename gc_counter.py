{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNvrSHYz9jYA1HwTMiRCt0v",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FarahhhFatima/human-genome-gc-counter/blob/main/gc_counter.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c368378e"
      },
      "source": [
        "# Task\n",
        "Calculate the GC content of a sample human chromosome (e.g., chromosome 1) by downloading its FASTA file, implementing functions to read FASTA and compute GC content, and then display the calculated GC content."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "460934ca"
      },
      "source": [
        "## Prepare Data Directory\n",
        "\n",
        "### Subtask:\n",
        "Create a dedicated directory to store the human genome FASTA files.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aba930e5"
      },
      "source": [
        "**Reasoning**:\n",
        "The subtask requires creating a directory to store FASTA files. I will use the `os` module to achieve this, defining a directory name and using `os.makedirs()` to create it, ensuring that existing directories do not raise an error.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "46b735a4",
        "outputId": "d107b8d8-67bc-461b-90f9-8660528ddfd2"
      },
      "source": [
        "import os\n",
        "\n",
        "# Define the directory name\n",
        "data_dir = 'data'\n",
        "\n",
        "# Create the directory if it doesn't already exist\n",
        "os.makedirs(data_dir, exist_ok=True)\n",
        "\n",
        "print(f\"Directory '{data_dir}' ensured to exist.\")"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Directory 'data' ensured to exist.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bea2caa3"
      },
      "source": [
        "## Download Sample Human Chromosome\n",
        "\n",
        "### Subtask:\n",
        "Download a sample human chromosome FASTA file (e.g., chromosome 1) from a public repository, such as UCSC, into the prepared data directory.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0f2aa8d6"
      },
      "source": [
        "**Reasoning**:\n",
        "To download the FASTA file, I will first define the URL and the local path, then use `wget` to download it and `gunzip` to decompress it. These are shell commands that can be executed within a Python notebook cell using `!`, leveraging the `data_dir` variable that has already been defined.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b45fe41a",
        "outputId": "958b7258-f1b9-4b26-ce5a-39f145f3199f"
      },
      "source": [
        "import os\n",
        "\n",
        "# Define the URL for human chromosome 1 FASTA file (hg38 assembly)\n",
        "ucsc_url = 'http://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chr1.fa.gz'\n",
        "\n",
        "# Construct the full path for saving the downloaded file\n",
        "# The data_dir variable was defined in a previous step.\n",
        "output_gz_file = os.path.join(data_dir, 'chr1.fa.gz')\n",
        "output_fa_file = os.path.join(data_dir, 'chr1.fa')\n",
        "\n",
        "# Download the file using wget\n",
        "print(f\"Downloading {ucsc_url} to {output_gz_file}...\")\n",
        "!wget -O {output_gz_file} {ucsc_url}\n",
        "\n",
        "# Decompress the .gz file using gunzip\n",
        "print(f\"Decompressing {output_gz_file}...\")\n",
        "!gunzip -f {output_gz_file}\n",
        "\n",
        "print(f\"File downloaded and decompressed to {output_fa_file}\")"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading http://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chr1.fa.gz to data/chr1.fa.gz...\n",
            "--2026-01-19 18:26:02--  http://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chr1.fa.gz\n",
            "Resolving hgdownload.cse.ucsc.edu (hgdownload.cse.ucsc.edu)... 128.114.119.163\n",
            "Connecting to hgdownload.cse.ucsc.edu (hgdownload.cse.ucsc.edu)|128.114.119.163|:80... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 74778116 (71M) [application/x-gzip]\n",
            "Saving to: ‘data/chr1.fa.gz’\n",
            "\n",
            "data/chr1.fa.gz     100%[===================>]  71.31M  42.8MB/s    in 1.7s    \n",
            "\n",
            "2026-01-19 18:26:04 (42.8 MB/s) - ‘data/chr1.fa.gz’ saved [74778116/74778116]\n",
            "\n",
            "Decompressing data/chr1.fa.gz...\n",
            "File downloaded and decompressed to data/chr1.fa\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5f12ff2e"
      },
      "source": [
        "## Implement GC Counter Functions\n",
        "\n",
        "### Subtask:\n",
        "Define the `read_fasta` and `calculate_gc` functions to process the downloaded FASTA file and compute the GC content.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "651c9a4d"
      },
      "source": [
        "**Reasoning**:\n",
        "I will define the `read_fasta` and `calculate_gc` functions as specified in the instructions. The `read_fasta` function will parse a FASTA file and return the sequence, while the `calculate_gc` function will compute the GC content of a given sequence. I'll include comments to explain the logic and ensure error handling for division by zero in `calculate_gc`.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fde1201d",
        "outputId": "90bd62a5-ac81-47b6-c58e-55834f057e8f"
      },
      "source": [
        "def read_fasta(file_path):\n",
        "    \"\"\"\n",
        "    Reads a FASTA file and returns the concatenated sequence.\n",
        "    Skips header lines (starting with '>').\n",
        "    \"\"\"\n",
        "    sequence = []\n",
        "    with open(file_path, 'r') as f:\n",
        "        for line in f:\n",
        "            line = line.strip()\n",
        "            if line and not line.startswith('>'):\n",
        "                sequence.append(line)\n",
        "    return ''.join(sequence)\n",
        "\n",
        "def calculate_gc(sequence):\n",
        "    \"\"\"\n",
        "    Calculates the GC content of a DNA sequence.\n",
        "    Counts G and C bases (case-insensitive) and total valid bases (A, T, G, C).\n",
        "    Returns GC content as a percentage.\n",
        "    \"\"\"\n",
        "    if not sequence:\n",
        "        return 0.0\n",
        "\n",
        "    gc_count = 0\n",
        "    total_bases = 0\n",
        "\n",
        "    for base in sequence:\n",
        "        upper_base = base.upper()\n",
        "        if upper_base in ('A', 'T', 'G', 'C'):\n",
        "            total_bases += 1\n",
        "            if upper_base in ('G', 'C'):\n",
        "                gc_count += 1\n",
        "\n",
        "    if total_bases == 0:\n",
        "        return 0.0\n",
        "\n",
        "    gc_content = (gc_count / total_bases) * 100\n",
        "    return gc_content\n",
        "\n",
        "print(\"Functions `read_fasta` and `calculate_gc` defined.\")"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Functions `read_fasta` and `calculate_gc` defined.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7158b7a6"
      },
      "source": [
        "## Calculate and Display GC Content\n",
        "\n",
        "### Subtask:\n",
        "Use the implemented functions to read the downloaded chromosome FASTA file, calculate its GC content, and then print the result.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b6701dcc"
      },
      "source": [
        "**Reasoning**:\n",
        "I will use the previously defined `read_fasta` and `calculate_gc` functions to process the downloaded FASTA file and display its GC content, as specified in the subtask instructions.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1195e41e",
        "outputId": "62579269-2b8c-4fe0-d78a-392d4ebe98f1"
      },
      "source": [
        "chromosome_sequence = read_fasta(output_fa_file)\n",
        "gc_content = calculate_gc(chromosome_sequence)\n",
        "\n",
        "print(f\"GC Content of Human Chromosome 1 (hg38) is: {gc_content:.2f}%\")"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "GC Content of Human Chromosome 1 (hg38) is: 41.72%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "05b4a0f1"
      },
      "source": [
        "## Final Task\n",
        "\n",
        "### Subtask:\n",
        "Summarize the project setup and the calculated GC content for the sample human chromosome.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3440d01b"
      },
      "source": [
        "## Summary:\n",
        "\n",
        "### Q&A\n",
        "The project setup involved creating a `data` directory, downloading the human chromosome 1 FASTA file (hg38 assembly) from UCSC, and decompressing it. The calculated GC content for Human Chromosome 1 (hg38) is 41.72%.\n",
        "\n",
        "### Data Analysis Key Findings\n",
        "*   A dedicated `data` directory was successfully created to store genomic sequence files.\n",
        "*   The FASTA file for human chromosome 1 (hg38 assembly), `chr1.fa.gz`, was successfully downloaded from the UCSC public repository.\n",
        "*   The downloaded compressed file was successfully decompressed to `chr1.fa` within the `data` directory.\n",
        "*   Two essential functions were implemented: `read_fasta` to parse FASTA files and extract the sequence, and `calculate_gc` to compute the GC content percentage from a given DNA sequence.\n",
        "*   Using these functions, the GC content of Human Chromosome 1 (hg38) was calculated to be 41.72%.\n",
        "\n",
        "### Insights or Next Steps\n",
        "*   The calculated GC content of 41.72% for human chromosome 1 is a fundamental genomic characteristic that can be used for comparative genomics or further sequence analysis.\n",
        "*   The established pipeline for downloading, parsing, and calculating GC content can be readily expanded to analyze other chromosomes, different species, or to implement more sophisticated sequence analysis techniques.\n"
      ]
    }
  ]
}