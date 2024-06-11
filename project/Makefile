# Python interpreter
PYTHON = python3

# Source file
SRC = project1.py

# Executable name
EXEC = MWST

# Default target
all: $(EXEC)

# Rule to create an executable script
$(EXEC): $(SRC)
	echo "#!/usr/bin/env $(PYTHON)" > $(EXEC)
	cat $(SRC) >> $(EXEC)
	chmod +x $(EXEC)

# Clean up
clean:
	rm -f $(EXEC)
