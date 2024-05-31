=========detection.py==========
python detection.py --network ./dataset/TC1-1 --mode normal&
python detection.py --network ./dataset/TC1-6 --mode normal&

python detection.py --network ./dataset/TC1-2 --mode normal&
python detection.py --network ./dataset/TC1-3 --mode normal&
python detection.py --network ./dataset/TC1-4 --mode normal&
python detection.py --network ./dataset/TC1-5 --mode normal&
python detection.py --network ./dataset/TC1-7 --mode normal&
python detection.py --network ./dataset/TC1-8 --mode normal&
python detection.py --network ./dataset/TC1-9 --mode normal&
python detection.py --network ./dataset/TC1-10 --mode normal&

python detection.py --network ./dataset/TC2-1 --mode normal&
python detection.py --network ./dataset/TC2-2 --mode normal&
python detection.py --network ./dataset/TC2-3 --mode normal&
python detection.py --network ./dataset/TC2-4 --mode normal&
python detection.py --network ./dataset/TC2-5 --mode normal&

python detection.py --network ./dataset/real/amazon --mode tree&
python detection.py --network ./dataset/real/dblp --mode tree&
python detection.py --network ./dataset/real/livejounal --mode tree&
python detection.py --network ./dataset/real/orkut --mode tree&

python detection.py --network ./dataset/real/dolphin --mode normal&
python detection.py --network ./dataset/real/football --mode normal&
python detection.py --network ./dataset/real/karate --mode normal&
python detection.py --network ./dataset/real/mexican --mode normal&
python detection.py --network ./dataset/real/polbooks --mode normal&
python detection.py --network ./dataset/real/railway --mode normal&
python detection.py --network ./dataset/real/strike --mode normal&

==========general_evaluation.py==========
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./louvain/TC1-1.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./louvain/TC1-1.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./louvain/TC1-2.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./louvain/TC1-2.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./louvain/TC1-3.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./louvain/TC1-3.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./louvain/TC1-4.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./louvain/TC1-4.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./louvain/TC1-5.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./louvain/TC1-5.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./louvain/TC1-6.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./louvain/TC1-6.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./louvain/TC1-7.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./louvain/TC1-7.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./louvain/TC1-8.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./louvain/TC1-8.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./louvain/TC1-9.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./louvain/TC1-9.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/dolphin/dolphin.cmty --detected ./louvain/dolphin.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/dolphin/dolphin.cmty --detected ./louvain/dolphin.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/football/football.cmty --detected ./louvain/football.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/football/football.cmty --detected ./louvain/football.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/karate/karate.cmty --detected ./louvain/karate.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/karate/karate.cmty --detected ./louvain/karate.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/mexican/mexican.cmty --detected ./louvain/mexican.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/mexican/mexican.cmty --detected ./louvain/mexican.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/polbooks/polbooks.cmty --detected ./louvain/polbooks.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/polbooks/polbooks.cmty --detected ./louvain/polbooks.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/strike/strike.cmty --detected ./louvain/strike.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/strike/strike.cmty --detected ./louvain/strike.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/coauthorship/coauthorship.cmty --detected ./louvain/coauthorship.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/coauthorship/coauthorship.cmty --detected ./louvain/coauthorship.cmty --algorithm louvain&
python general_evaluation.py --measure nmi --ground ./groundtruth/railway/railway.cmty --detected ./louvain/railway.cmty --algorithm louvain&
python general_evaluation.py --measure f1 --ground ./groundtruth/railway/railway.cmty --detected ./louvain/railway.cmty --algorithm louvain&

python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./leiden/TC1-1.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./leiden/TC1-1.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./leiden/TC1-2.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./leiden/TC1-2.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./leiden/TC1-3.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./leiden/TC1-3.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./leiden/TC1-4.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./leiden/TC1-4.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./leiden/TC1-5.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./leiden/TC1-5.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./leiden/TC1-6.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./leiden/TC1-6.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./leiden/TC1-7.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./leiden/TC1-7.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./leiden/TC1-8.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./leiden/TC1-8.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./leiden/TC1-9.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./leiden/TC1-9.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-10/TC1-10.cmty --detected ./leiden/TC1-10.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-10/TC1-10.cmty --detected ./leiden/TC1-10.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/dolphin/dolphin.cmty --detected ./leiden/dolphin.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/dolphin/dolphin.cmty --detected ./leiden/dolphin.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/football/football.cmty --detected ./leiden/football.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/football/football.cmty --detected ./leiden/football.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/karate/karate.cmty --detected ./leiden/karate.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/karate/karate.cmty --detected ./leiden/karate.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/mexican/mexican.cmty --detected ./leiden/mexican.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/mexican/mexican.cmty --detected ./leiden/mexican.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/polbooks/polbooks.cmty --detected ./leiden/polbooks.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/polbooks/polbooks.cmty --detected ./leiden/polbooks.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/strike/strike.cmty --detected ./leiden/strike.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/strike/strike.cmty --detected ./leiden/strike.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/coauthorship/coauthorship.cmty --detected ./leiden/coauthorship.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/coauthorship/coauthorship.cmty --detected ./leiden/coauthorship.cmty --algorithm leiden&
python general_evaluation.py --measure nmi --ground ./groundtruth/railway/railway.cmty --detected ./leiden/railway.cmty --algorithm leiden&
python general_evaluation.py --measure f1 --ground ./groundtruth/railway/railway.cmty --detected ./leiden/railway.cmty --algorithm leiden&


python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./output/TC1-1/TC1-1.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./output/TC1-1/TC1-1.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./output/TC1-2/TC1-2.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./output/TC1-2/TC1-2.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./output/TC1-3/TC1-3.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./output/TC1-3/TC1-3.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./output/TC1-4/TC1-4.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./output/TC1-4/TC1-4.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./output/TC1-5/TC1-5.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./output/TC1-5/TC1-5.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./output/TC1-6/TC1-6.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./output/TC1-6/TC1-6.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./output/TC1-7/TC1-7.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./output/TC1-7/TC1-7.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./output/TC1-8/TC1-8.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./output/TC1-8/TC1-8.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./output/TC1-9/TC1-9.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./output/TC1-9/TC1-9.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-10/TC1-10.cmty --detected ./output/TC1-10/TC1-10.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-10/TC1-10.cmty --detected ./output/TC1-10/TC1-10.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/dolphin/dolphin.cmty --detected ./new_output/dolphin/dolphin.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/dolphin/dolphin.cmty --detected ./new_output/dolphin/dolphin.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/football/football.cmty --detected ./new_output/football/football.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/football/football.cmty --detected ./new_output/football/football.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/karate/karate.cmty --detected ./new_output/karate/karate.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/karate/karate.cmty --detected ./new_output/karate/karate.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/mexican/mexican.cmty --detected ./new_output/mexican/mexican.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/mexican/mexican.cmty --detected ./new_output/mexican/mexican.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/polbooks/polbooks.cmty --detected ./new_output/polbooks/polbooks.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/polbooks/polbooks.cmty --detected ./new_output/polbooks/polbooks.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/strike/strike.cmty --detected ./new_output/strike/strike.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/strike/strike.cmty --detected ./new_output/strike/strike.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/railway/railway.cmty --detected ./new_output/railway/railway.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/railway/railway.cmty --detected ./new_output/railway/railway.cmty --algorithm ours&

python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./label_propagation/TC1-6.cmty --algorithm label_propagation&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./label_propagation/TC1-1.cmty --algorithm label_propagation&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./label_propagation/TC1-6.cmty --algorithm label_propagation&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./label_propagation/TC1-1.cmty --algorithm label_propagation&
python general_evaluation.py --measure purity --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./label_propagation/TC1-6.cmty --algorithm label_propagation&
python general_evaluation.py --measure purity --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./label_propagation/TC1-1.cmty --algorithm label_propagation&

python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./old_output/TC1-1/TC1-1.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./old_output/TC1-1/TC1-1.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./old_output/TC1-2/TC1-2.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-2/TC1-2.cmty --detected ./old_output/TC1-2/TC1-2.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./old_output/TC1-3/TC1-3.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-3/TC1-3.cmty --detected ./old_output/TC1-3/TC1-3.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./old_output/TC1-4/TC1-4.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-4/TC1-4.cmty --detected ./old_output/TC1-4/TC1-4.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./old_output/TC1-5/TC1-5.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-5/TC1-5.cmty --detected ./old_output/TC1-5/TC1-5.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./new_output/TC1-6/TC1-6.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./new_output/TC1-6/TC1-6.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./old_output/TC1-7/TC1-7.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-7/TC1-7.cmty --detected ./old_output/TC1-7/TC1-7.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./old_output/TC1-8/TC1-8.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-8/TC1-8.cmty --detected ./old_output/TC1-8/TC1-8.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./old_output/TC1-9/TC1-9.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-9/TC1-9.cmty --detected ./old_output/TC1-9/TC1-9.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/TC1-10/TC1-10.cmty --detected ./new_output/TC1-10/TC1-10.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/TC1-10/TC1-10.cmty --detected ./new_output/TC1-10/TC1-10.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/dolphin/dolphin.cmty --detected ./old_output/dolphin/dolphin.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/dolphin/dolphin.cmty --detected ./old_output/dolphin/dolphin.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/football/football.cmty --detected ./old_output/football/football.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/football/football.cmty --detected ./old_output/football/football.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/karate/karate.cmty --detected ./old_output/karate/karate.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/karate/karate.cmty --detected ./old_output/karate/karate.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/mexican/mexican.cmty --detected ./old_output/mexican/mexican.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/mexican/mexican.cmty --detected ./old_output/mexican/mexican.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/polbooks/polbooks.cmty --detected ./old_output/polbooks/polbooks.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/polbooks/polbooks.cmty --detected ./old_output/polbooks/polbooks.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/strike/strike.cmty --detected ./old_output/strike/strike.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/strike/strike.cmty --detected ./old_output/strike/strike.cmty --algorithm ours&
python general_evaluation.py --measure nmi --ground ./groundtruth/railway/railway.cmty --detected ./old_output/railway/railway.cmty --algorithm ours&
python general_evaluation.py --measure f1 --ground ./groundtruth/railway/railway.cmty --detected ./old_output/railway/railway.cmty --algorithm ours&

==========draw.py==========
python draw.py --mode community_purity --data TC1-1#TC1-6 --algorithm louvain#ours&
python draw.py --mode community_purity --data TC1-1 --algorithm louvain#label_propagation#ours&
python draw.py --mode community_purity --data TC1-6 --algorithm louvain#label_propagation#ours&
python draw.py --mode seed --data TC1-1#TC1-6&

python draw.py --mode nmi --data TC1-1#TC1-6 --algorithm louvain#leiden#label_propagation#ours&
python draw.py --mode f1 --data TC1-1#TC1-6 --algorithm louvain#leiden#label_propagation#ours&

python draw.py --mode nmilong --algorithm louvain#leiden#ours&

python draw.py --mode num_community --data TC1-6#TC1-10#football#mexican#strike&

python draw.py --mode distribution --data TC1-1#TC1-6 --algorithm louvain#ours

python draw.py --mode distribution --data TC1-6 --algorithm louvain#ours&

python draw.py --mode distribution --data TC1-6 --algorithm louvain#leiden#label_propagation#ours&
python draw.py --mode distribution --data TC1-1 --algorithm louvain#leiden#label_propagation#ours&
python draw.py --mode distribution --data TC1-6 --algorithm label_propagation#ours&
python draw.py --mode distribution --data TC1-1 --algorithm leiden#ours&

python draw.py --mode scalability --data TC2-1#TC2-2#TC2-3#TC2-4#TC2-5&

python draw.py --mode f1long --algorithm louvain#leiden#ours

==========others.py==========
python others.py --networkFile ./dataset/TC1-6/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-1/network.txt --algorithm label_propagation&
python others.py --networkFile ./dataset/TC1-6/network.txt --algorithm infomap&
python others.py --networkFile ./dataset/TC1-10/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-10/network.txt --algorithm louvain&


python others.py --networkFile ./dataset/TC1-2/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/TC1-3/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/TC1-4/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/TC1-5/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/TC1-7/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/TC1-8/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/TC1-9/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/coauthorship/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/dolphin/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/football/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/karate/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/mexican/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/polbooks/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/railway/network.txt --algorithm louvain&
python others.py --networkFile ./dataset/real/strike/network.txt --algorithm louvain&

python others.py --networkFile ./dataset/real/find/dblp/network.txt --algorithm leiden&

python others.py --networkFile ./dataset/TC1-2/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-3/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-4/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-5/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-7/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-8/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/TC1-9/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/coauthorship/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/dolphin/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/football/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/karate/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/mexican/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/polbooks/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/railway/network.txt --algorithm leiden&
python others.py --networkFile ./dataset/real/strike/network.txt --algorithm leiden&


python others.py --networkFile ./dataset/real/find/livejounal/network.txt --algorithm leiden&

python others.py --networkFile ./dataset/real/find/livejounal/network.txt --algorithm louvain&
