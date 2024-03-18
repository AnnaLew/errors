#!/bin/bash

# Check if correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 input_directory"
    exit 1
fi

# Define the input directory
input_directory="$1"

for subdirectory in "$input_directory"/*/; do
    
    # Extract the folder name (group name)
    folder_name=$(basename "$subdirectory")

    echo "$folder_name"

    for input_file in "$subdirectory"/*/*.gbk; do

        # Extract the file name and genome name
        file_name=$(basename "$input_file")

        genome_name="${file_name%.*}"

        # Extract the ref_accnum from the first line of the .gbk file
        ref_accnum=$(head -n 1 "$input_file" | awk '{print $2}')

        echo "$genome_name"
        echo "ref_accnum: $ref_accnum"

        # Call Python script with ref_accnum
        python islandviewer.py "$input_file" "$genome_name $folder_name" "$ref_accnum"

    done
done
