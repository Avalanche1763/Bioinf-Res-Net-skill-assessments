#Answers to questions from "Linux for Bioinformatics"

Q1: What is your home directory?

A: /home/ubuntu

Q2: What is the output of this command?

A: hello_world.txt

Q3: What is the output of each `ls` command?

A: output for my_folder/ : (empty)
   output for my_folder2/: hello_world.txt

Q4: What is the output of each?

A: output for my_folder/ : (empty)
   output for my_folder2/: (empty)
   output for my_folder3/: hello_world.txt

Q5: What editor did you use and what was the command to save your file changes?

A: vim, saved with the command `wq!`

Q6: What is the error?

A: Permission denied (publickey).

Q7: What was the solution?

A: Copy authorized_keys to /home/sudouser/.ssh/ , then use chown to make /.ssh/ contents be owned by sudouser, and chmod 600 to make authorized_keys only readable by sudouser

Q8: what does the `sudo docker run` part of the command do? and what does the `salmon swim` part of the command do?

A: `sudo docker run` together tells the machine to run the following command in a docker container, sudo is needed because sudouser is not added to the docker group yet. `salmon swim` is the 'super-secret operation' command, which prints a version check (though it may be outdated, mine says "Version Server Response: Not Found") and the ASCII rendering of "Salmon" in the terminal.

Q9: What is the output of this command?

A: serveruser is not in the sudoers file

Q10: What is the output of `flask --version`?

A:  Python 3.12.7
    Flask 3.0.3
    Werkzeug 3.1.3

Q11: What is the output of `mamba -V`?

A:  mamba 1.5.9
    conda 24.9.2

Q12: What is the output of `which python`?

A: /home/serveruser/miniforge3/envs/py27/bin/python

Q13: What is the output of `which python` now?

A: /home/serveruser/miniforge3/bin/python

Q14: What is the output of `salmon -h`?

A:
salmon v1.4.0

Usage:  salmon -h|--help or
        salmon -v|--version or
        salmon -c|--cite or
        salmon [--no-version-check] <COMMAND> [-h | options]

Commands:
     index      : create a salmon index
     quant      : quantify a sample
     alevin     : single cell analysis
     swim       : perform super-secret operation
     quantmerge : merge multiple quantifications into a single file

Q15: What does the `-o athal.fa.gz` part of the command do?

A: Specifies the file that content from the url will be written to, here we specify to writie it to `athal.fa.gz`.

Q16: What is a `.gz` file?

A: A file compressed with gzip.

Q17: What does the `zcat` command do?

A: Cats a compressed file.

Q18: what does the `head` command do?

A: Prints only the first 10 lines of the specified file, here piped to the command.

Q19: what does the number `100` signify in the command?

A: Using the `-n` operator followed by a number allows the user to specify the number of lines shown using head. `-n 100` shows the first 100 lines.

Q20: What is `|` doing?

A: Taking the output of the curl command as input for the head command.

Q21: What is a `.fa` file? What is this file format used for?

A: A `.fa` file signifies the FASTA format in this case, which is used for nucleotide sequences and amino acid sequences, representing one base/residue as one letter. It is used for bioinformatic analysis of such data.

Q22: What format are the downloaded sequencing reads in?

A: The downloaded file is in `.sra` format, indicating that it is a Sequence Read Archive, in this case.

Q23: What is the total size of the disk?

A: 6.8 G

Q24: How much space is remaining on the disk?

A: 1.5 G

Q25: What went wrong?

A: Ran out of disk space with the following error `err: storage exhausted while writing file within file system module - system bad file descriptor error fd='5'`

Q26: What was your solution?

A: Use option --gzip to compress output.
