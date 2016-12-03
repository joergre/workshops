	CLEANUP = rm -f
# Befehl der bei clean ausgeführt wird (alles löschen)
	MKDIR = mkdir -p
# Befehl der bei MKDIR ausgeführt wird. "-p" erzeugt keinen Fehler, wenn das Verzeichnis bereits existiert und legt notfalls Übergrordnete Verzeichnisse selbständig an.
	TARGET_EXTENSION=.out
# Die fertig kompilierte Datei endet auf .out	
	
#Tool Definitions
CC=gcc
# Compiler gcc
CFLAGS=-I. -I$(PATHU) -DTEST
# CFLAGS	Compiler-Optionen _ -I. (http://tigcc.ticalc.org/doc/comopts.html#SEC45): Gibt an, in welchen Verzeichnissen (cpath) nachheader-Dateien gesucht werden soll.
# -I$(PATHU): Hinzugefügt wird das Verzeichnis ../Unity/src zu cpath
# 

#Path Definitions
PATHU = ../Unity/src/
PATHS =
PATHT =
PATHB = build/

#Files We Are To Work With
SRC = testUnit1.c unity.c
OBJ = $(patsubst %.c,$(PATHB)%.o,$(SRC))
DEP = $(PATHU)unity.h $(PATHU)unity_internals.h
TGT = $(PATHB)test$(TARGET_EXTENSION)

test: $(PATHB) $(TGT)
	./$(TGT)

$(PATHB)%.o:: $(PATHS)%.c $(DEP)
	$(CC) -c $(CFLAGS) $< -o $@

$(PATHB)%.o:: $(PATHU)%.c $(DEP)
	$(CC) -c $(CFLAGS) $< -o $@

$(TGT): $(OBJ)
	gcc -o $@ $^

clean:
	$(CLEANUP) $(PATHB)*.o
	$(CLEANUP) $(TGT)

$(PATHB):
	$(MKDIR) $(PATHB)

all: clean test

.PHONY: all
.PHONY: clean
.PHONY: test
# Der Befehl all, clean oder test wird ausgefüht unabhängig ob die Datei all, clean oder test existiert (http://www.ijon.de/comp/tutorials/makefile.html#phony)

