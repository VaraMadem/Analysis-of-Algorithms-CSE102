PYTHON = python3

# Source files
SRC = project1.py

# Executable name
EXEC = MWST

# Default target
all: $(EXEC)

# Rule to create an executable script
$(EXEC): $(SRC)
	echo "/usr/local/bin/$(PYTHON) project1.py" > $(EXEC)
	chmod +x $(EXEC)

# Clean up
clean:
	rm -f $(EXEC)
