
.PHONY: clean


clean:
	find . -name "*.o" -print0 | xargs -0 rm -f
	find . -name "*.d" -print0 | xargs -0 rm -f
	find . -name "*.a" -print0 | xargs -0 rm -f
	rm -f lib/*
	rm -f prog*

