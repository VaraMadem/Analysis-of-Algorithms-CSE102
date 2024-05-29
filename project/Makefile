PYTHON = python3

# Source files
SRC = main.py other.py

# Executable name
EXEC = MWST

# Default target
all: $(EXEC)

# Rule to create an executable script
$(EXEC): $(SRC)
    echo "#!/bin/bash\$(PYTHON) main.py" > $(EXEC)
    chmod +x $(EXEC)

# Clean up
clean:
    rm -f $(EXEC)

