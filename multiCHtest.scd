///from the video on patterns

s.boot;


(
SynthDef.new(\sine, {
	arg freq=440, atk=0.005, rel=0.3, amp=1, pan=0;
	var sig, env;
	sig = SinOsc.ar(freq);
	env = EnvGen.kr(Env.new([0,1,0],[atk,rel],[1,-1]),doneAction:2);
	sig = sig * env;
	Out.ar(0, sig);
}).add;
)

Synth.new(\sine);

(
p = Pbind(
	\instrument, \sine,
	\dur, 0.3,//Pseq([0.6, 0.15, 0.15, 0.2], inf).trace,
	\freq, Pseq([220, 330, 264, 220, 440, 330], inf).trace,
).play;
)

s.plotTree;

p.stop;



//next part, so cool

(
SynthDef.new(\sine, {
	arg freq=440, atk=0.005, rel=0.3, amp=1, pan=0;
	var sig, env;
	sig = SinOsc.ar(freq);
	env = EnvGen.kr(Env.new([0,1,0],[atk,rel],[1,-1]),doneAction:2);
	sig = sig * env;
	Out.ar(0, sig);
}).add;
)

Synth.new(\sine);

(
p = Pbind(
	\instrument, \sine,
	\dur, Pwhite(0.05, 0.5, inf),
	\midinote, 24,
	\harmonic, Pexprand(1, 88, inf).round.trace,
	\atk, Pwhite(1.0, 3.0, inf),
	\rel, Pwhite(2.0, 1.0, inf),
	\amp, Pkey(\harmonic).reciprocal * 0.3,
	\pan, Pwhite(-0.8, 0.8, inf),
).play;
)

s.plotTree;

p.stop;


// patching input to output

(
SynthDef("help-AudioIn",{ arg out=0;
Out.ar(0,
        PingPong.ar(bufnum, [0,1] *  EnvGen.kr(Env([1, 1, 0], [2, 0.1])),
            0.1, 0.8, 1)
    )
}).play;
)


//guitar input stuff
// scope input; silent output
{ Amplitude.kr(SoundIn.ar(0)); }.scope;


{FreeVerb.ar(SoundIn.ar([0,1]).distort)}.play

{FreeVerb.ar(SoundIn.ar([0,1]).distort,0.8,0.6,0.3,1,0)}.play

{PingPong.ar(SoundIn.ar([0,1]).distort)}.play //broke'

{AllpassL.ar(SoundIn.ar([0,1]).distort)}.play

{SoundIn.ar(0).distort}.play;


s.boot;
o = Server.local.options;
o.devices
o.maxSynthDefs
o.inputStreamsEnabled
o.inDevice = "MOTU UltraLite mk3 Hybrid";
o.inDevice
o.outDevice = "Built-in Output";
o.outDevice = "MOTU UltraLite mk3 Hybrid";
inDevices;
s.freeAll
s.plotTree;
s.quit;
p.stop;
s.meter;

(
x = {
	var sig, amp;
	amp = SinOsc.kr([5,2,1,0.5,0.2]).range(0,1);
	sig = SinOsc.ar([300,500,700,900,1100]);
	sig = sig*amp;
}.play
)