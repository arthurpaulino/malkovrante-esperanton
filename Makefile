.PHONY: compile clean

compile:
	@python3 compile.py && pdflatex malkovrante-esperanton.tex

clean:
	@rm *.aux *.log *.pdf content.tex
