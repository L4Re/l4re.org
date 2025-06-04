LOG_FILES = arm_altra80_el1_ipc.logdata arm_altra80_el2_ipc.logdata \
	    x86_xeon_gold_6248R_2socket_all.logdata \
	    x86_xeon_gold_6248R_2socket_noht.logdata \
	    x86_n100.logdata

GEN_FILES = $(patsubst %.logdata,%.html,$(addprefix gen/,$(LOG_FILES)))

all: $(GEN_FILES)

clean:
	rm -fr gen

gen/%.html: logdata/%.logdata gen_chart_js Makefile
	@mkdir -p $(@D)
	./gen_chart_js $< > $@
