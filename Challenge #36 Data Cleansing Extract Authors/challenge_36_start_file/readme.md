﻿The link to the solution for last challenge #35 is  [HERE](https://community.alteryx.com/t5/Weekly-Challenge/Weekly-Exercise-35-Data-Cleansing-Practice-Beginner/m-p/36438#U36438).

Use Case: An analytical consulting company downloads medical journal publication data from the web and would like to extract all of the authors for the listed entries.

The text input contains details about each article where FAU indicates the author name for the article – in most case there are multiple authors. The details of each article are contained in lines that begin with PMID and end with an empty line.

Objective: Parse out each article PMID and list each author in sequential columns as seen in the Results.yxmd file.

**Input**


|  Name   |   Type   |
|---------|----------|
| Field_1 | V_String |

**Output**


|   Name    |   Type   |
|-----------|----------|
| PMID      | String   |
| Author1   | V_String |
| Author2   | V_String |
| Author3   | V_String |
| Author4   | V_String |
| Author5   | V_String |
| Author6   | V_String |
| Author7   | V_String |
| Author8   | V_String |
| Author9   | V_String |
| Author10  | V_String |
| Author11  | V_String |
| Author12  | V_String |
| Author13  | V_String |
| Author14  | V_String |
| Author15  | V_String |
| Author16  | V_String |
| Author17  | V_String |
| Author18  | V_String |
| Author19  | V_String |
| Author20  | V_String |
| Author21  | V_String |
| Author22  | V_String |
| Author23  | V_String |
| Author24  | V_String |
| Author25  | V_String |
| Author26  | V_String |
| Author27  | V_String |
| Author28  | V_String |
| Author29  | V_String |
| Author30  | V_String |
| Author31  | V_String |
| Author32  | V_String |
| Author33  | V_String |
| Author34  | V_String |
| Author35  | V_String |
| Author36  | V_String |
| Author37  | V_String |
| Author38  | V_String |
| Author39  | V_String |
| Author40  | V_String |
| Author41  | V_String |
| Author42  | V_String |
| Author43  | V_String |
| Author44  | V_String |
| Author45  | V_String |
| Author46  | V_String |
| Author47  | V_String |
| Author48  | V_String |
| Author49  | V_String |
| Author50  | V_String |
| Author51  | V_String |
| Author52  | V_String |
| Author53  | V_String |
| Author54  | V_String |
| Author55  | V_String |
| Author56  | V_String |
| Author57  | V_String |
| Author58  | V_String |
| Author59  | V_String |
| Author60  | V_String |
| Author61  | V_String |
| Author62  | V_String |
| Author63  | V_String |
| Author64  | V_String |
| Author65  | V_String |
| Author66  | V_String |
| Author67  | V_String |
| Author68  | V_String |
| Author69  | V_String |
| Author70  | V_String |
| Author71  | V_String |
| Author72  | V_String |
| Author73  | V_String |
| Author74  | V_String |
| Author75  | V_String |
| Author76  | V_String |
| Author77  | V_String |
| Author78  | V_String |
| Author79  | V_String |
| Author80  | V_String |
| Author81  | V_String |
| Author82  | V_String |
| Author83  | V_String |
| Author84  | V_String |
| Author85  | V_String |
| Author86  | V_String |
| Author87  | V_String |
| Author88  | V_String |
| Author89  | V_String |
| Author90  | V_String |
| Author91  | V_String |
| Author92  | V_String |
| Author93  | V_String |
| Author94  | V_String |
| Author95  | V_String |
| Author96  | V_String |
| Author97  | V_String |
| Author98  | V_String |
| Author99  | V_String |
| Author100 | V_String |
| Author101 | V_String |
| Author102 | V_String |
| Author103 | V_String |
| Author104 | V_String |
| Author105 | V_String |
| Author106 | V_String |
| Author107 | V_String |
| Author108 | V_String |
| Author109 | V_String |
| Author110 | V_String |
| Author111 | V_String |
| Author112 | V_String |
| Author113 | V_String |
| Author114 | V_String |
| Author115 | V_String |
| Author116 | V_String |
| Author117 | V_String |
| Author118 | V_String |
| Author119 | V_String |
| Author120 | V_String |
| Author121 | V_String |
| Author122 | V_String |
| Author123 | V_String |
| Author124 | V_String |
| Author125 | V_String |
| Author126 | V_String |
| Author127 | V_String |
| Author128 | V_String |
| Author129 | V_String |
| Author130 | V_String |
| Author131 | V_String |
| Author132 | V_String |
| Author133 | V_String |
| Author134 | V_String |
| Author135 | V_String |
| Author136 | V_String |
| Author137 | V_String |
| Author138 | V_String |
| Author139 | V_String |
| Author140 | V_String |
| Author141 | V_String |
| Author142 | V_String |
| Author143 | V_String |
| Author144 | V_String |
| Author145 | V_String |
| Author146 | V_String |
| Author147 | V_String |
| Author148 | V_String |
| Author149 | V_String |
| Author150 | V_String |
| Author151 | V_String |
| Author152 | V_String |
| Author153 | V_String |
| Author154 | V_String |
| Author155 | V_String |
| Author156 | V_String |
| Author157 | V_String |
| Author158 | V_String |
| Author159 | V_String |
| Author160 | V_String |
| Author161 | V_String |
| Author162 | V_String |
| Author163 | V_String |
| Author164 | V_String |
| Author165 | V_String |
| Author166 | V_String |
| Author167 | V_String |
| Author168 | V_String |
| Author169 | V_String |
| Author170 | V_String |
| Author171 | V_String |
| Author172 | V_String |
| Author173 | V_String |
| Author174 | V_String |
| Author175 | V_String |
| Author176 | V_String |
| Author177 | V_String |
| Author178 | V_String |
| Author179 | V_String |
| Author180 | V_String |
| Author181 | V_String |
| Author182 | V_String |
| Author183 | V_String |
| Author184 | V_String |
| Author185 | V_String |
| Author186 | V_String |
| Author187 | V_String |
| Author188 | V_String |
| Author189 | V_String |
| Author190 | V_String |
| Author191 | V_String |
| Author192 | V_String |
| Author193 | V_String |
| Author194 | V_String |
| Author195 | V_String |
| Author196 | V_String |
| Author197 | V_String |
| Author198 | V_String |
| Author199 | V_String |
| Author200 | V_String |
| Author201 | V_String |
| Author202 | V_String |
| Author203 | V_String |
| Author204 | V_String |
| Author205 | V_String |
| Author206 | V_String |
| Author207 | V_String |
| Author208 | V_String |
| Author209 | V_String |
| Author210 | V_String |
| Author211 | V_String |
| Author212 | V_String |
| Author213 | V_String |
| Author214 | V_String |
| Author215 | V_String |
| Author216 | V_String |
| Author217 | V_String |
| Author218 | V_String |
| Author219 | V_String |
| Author220 | V_String |
| Author221 | V_String |
| Author222 | V_String |
| Author223 | V_String |
| Author224 | V_String |
| Author225 | V_String |
| Author226 | V_String |
| Author227 | V_String |
| Author228 | V_String |
| Author229 | V_String |
| Author230 | V_String |
| Author231 | V_String |
| Author232 | V_String |
| Author233 | V_String |
| Author234 | V_String |
| Author235 | V_String |
| Author236 | V_String |
| Author237 | V_String |
| Author238 | V_String |
| Author239 | V_String |
| Author240 | V_String |
| Author241 | V_String |
| Author242 | V_String |
| Author243 | V_String |
| Author244 | V_String |
| Author245 | V_String |
| Author246 | V_String |
| Author247 | V_String |
| Author248 | V_String |
| Author249 | V_String |
| Author250 | V_String |
| Author251 | V_String |
| Author252 | V_String |
| Author253 | V_String |
| Author254 | V_String |
| Author255 | V_String |
| Author256 | V_String |
| Author257 | V_String |
| Author258 | V_String |
| Author259 | V_String |
| Author260 | V_String |
| Author261 | V_String |
| Author262 | V_String |
| Author263 | V_String |
| Author264 | V_String |

