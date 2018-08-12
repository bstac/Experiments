//http://vimeo.com/71100719

//not my code

//When an Array is given as an input to a unit generator it causes
//an array of multiple copies of that unit generator to be made,
//each with a different value from the input array. This is called
//multichannel expansion. All but a few special unit generators
//perform multichannel expansion. Only Arrays are expanded, no
//other type of Collection, not even subclasses of Array.

//relationships
//amp = 1/r
//reverb = r
//speaker value =

s.boot;
s.freeAll;
s.quit;


(
SynthDef('funsynth', {
	arg pitch=200;
	var sound = SinOsc.ar(pitch, mul:0.2);
	var linen = Env.linen(0.01, sustainTime:0, releasetime:1);
	var env = EnvGen.kr(linen, doneAction:2);
	Out.ar(0, sound * env);
}).add;
)



NetAddr.localAddr

(
OSCdef('cubeListener',
	{
		arg msg;
		Synth('funsynth', [pitch:(msg[1]*100+50)]);
	},
	"/cube");
)

//this is for the dome, 5 speakers
//synth structure is taken from video 3 of
//the youtube SC tutorial series.
//i went back to learn about synths,
//and it turns out they were using reverb and everything i wanted
//to control
//this is the updated one, for what i need
//ps, pretend Hz stands for decibals.
//i screwed up when i named it and im in a rush
(
SynthDef.new(\pulseTest, {
	arg rate=2, ampHz1=1, ampHz2=1, ampHz3=1, ampHz4=1, ampHz5=1,fund=40, maxPartial=4, width=0.5, revb=0.5;
	var  sig1, sig2, sig3, sig4, sig5, amp1, amp2, amp3, amp4, amp5, freq, rev;
	rev = revb;
	amp1 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz1;
	amp2 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz2;
	amp3 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz3;
	amp4 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz4;
	amp5 = LFPulse.kr(rate, 0.5, 0.12) * 0.2 * ampHz5;
	freq = LFNoise0.kr(4).exprange(fund, fund*maxPartial).round(fund);
	freq = freq * LFPulse.kr(8, add:1);
	sig1 = Pulse.ar(freq, width, amp1);
	sig2 = Pulse.ar(freq, width, amp2);
	sig3 = Pulse.ar(freq, width, amp3);
	sig4 = Pulse.ar(freq, width, amp4);
	sig5 = Pulse.ar(freq, width, amp5);
	sig1 = FreeVerb.ar(sig1, rev, rev, 0.25);
	sig2 = FreeVerb.ar(sig2, rev, rev, 0.25);
	sig3 = FreeVerb.ar(sig3, rev, rev, 0.25);
	sig4 = FreeVerb.ar(sig4, rev, rev, 0.25);
	sig5 = FreeVerb.ar(sig5, rev, rev, 0.25);
	Out.ar(0, sig1);
	Out.ar(1, sig2);
	Out.ar(2, sig3);
	Out.ar(3, sig4);
	Out.ar(4, sig5);
}).add;
)

x = Synth.new(\pulseTest);

(
OSCdef('cubeListener',
	{
		arg msg;
		x.set(\revb, (msg[1]));
		x.set(\ampHz1, (msg[2]));
		x.set(\ampHz2, (msg[3]));
		x.set(\ampHz3, (msg[4]));
		x.set(\ampHz4, (msg[5]));
		x.set(\ampHz5, (msg[6]));
	},
	"/cube");
)


x.set(\fund, 47);
s.boot;
s.quit;
NetAddr.localAddr;
o = Server.local.options;
o.inDevice = "MOTU UltraLite mk3 Hybrid";
o.outDevice = "MOTU UltraLite mk3 Hybrid";
s.freeAll;
s.plotTree;
s.meter;

s.meter