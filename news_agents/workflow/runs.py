from news_agents.agents.summarizer_agent import SummarizerAgent
from news_agents.agents.sorter_agent import SorterAgent


def run_main_loop(
    summarizer: SummarizerAgent,
    sorter: SorterAgent,
) -> bool:
    summary = summarizer.get_file_summary(
        """Immediately after another media event held the following September, Apple removed almost all mentions of AirPower from its website.[5] There were reportedly several development issues that led to this decision, with heat management, inter-device communication and speed, as well as mechanical and interference issues all being rumored.[6] Reportedly, the main engineering issue came from including coils for two charging standards, as the Apple Watch uses a proprietary non-Qi standard.[7] Blogger John Gruber, known for his close connections with Apple, wrote that he had heard of issues with the device’s design: "Something about the multi-coil design getting too hot — way too hot. There are engineers who looked at AirPower’s design and said it could never work thermally."[8]

AirPower was still mentioned in the packaging of several Apple products, including iPhone XS and iPhone XR,[9] and in January 2019 media outlets reported that AirPower may have entered production.[10] On March 25, 2019, Apple released iOS 12.2 with support for AirPower. On March 26, 2019, Apple shipped the Wireless Charging Case for AirPods featuring AirPower on the packaging. Also in late March, Apple secured a trademark on the AirPower name.[11]

However, on March 29, 2019, Dan Riccio, Apple’s senior vice president of Hardware Engineering, said in a statement emailed to TechCrunch: "After much effort, we’ve concluded AirPower will not achieve our high standards and we have canceled the project."[12] The move was unprecedented for Apple as it had never previously canceled an announced hardware product.[13]"""
    )

    sorter_test = sorter.sort_headlines(
        """Russia says Wagner Group’s leader will move to Belarus after his rebellious march challenged Putin
The ultra-wealthy have dangerous pastimes. Who pays when they need saving?
Orca pod attacks Ocean Race boats
Four players suspended after hostile soccer game between US and Mexico
Israeli military kills Palestinian gunman as settlers rampage through Palestinian town
Packages from China are surging into the United States. Some say $800 duty-free limit was a mistake
One year later, the Supreme Court’s abortion decision is both scorned and praised
Speaker McCarthy supports expunging Trump’s impeachments over Ukraine and Jan. 6"""
    )
