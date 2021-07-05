from typing import Sequence

from numpy import column_stack
import streamlit as st
import pandas as pd
import altair as alt

st.title(
    '''
    DNA COUNTER APP
    '''
)
st.header("DNA Sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence= '-'.join(sequence)

st.write("***")
st.header("INPUT(DNA QUERY)")
sequence
st.write("****")
st.header("OUTPUT(NUMBER OF VARIOUS COMPONENT)")

def count_comp(seq):
    d = dict([
        ('A',seq.count('A')),
        ('G',seq.count('G')),
        ('C',seq.count('C')),
        ('T',seq.count('T'))
    ])
    return d

X = count_comp(sequence)
X

st.header("2. Plain Text")
st.write('There are '+str(X['A'])+' Acetocine(A)')
st.write('There are '+str(X['C'])+' Cytosine(C)')
st.write('There are '+str(X['G'])+' Guanine(G)')
st.write('There are '+str(X['T'])+' Thymine(T)')

st.header("3. Dataframe")
df = pd.DataFrame.from_dict(X,orient='index')
df=df.rename({0:'count'},axis=1)
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'Nucleotide'})
st.write(df)

st.header("4. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y = 'count'
)
p=p.properties(
    width=alt.Step(80)
)
st.write(p)