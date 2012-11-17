PAGES = $(patsubst _templates/%,%,$(wildcard _templates/*.html))

build: $(PAGES)

%.html: _templates/%.html
	@./_tools/build_pages "$<"
